from binascii import hexlify, unhexlify

from bitcoin.core.script import CScript, SignatureHash, SIGHASH_ALL
from bitcoin.core import lx, b2lx, COutPoint, CTxIn, CTxOut, CTransaction
from bitcoin.core.serialize import Hash

from coinop.bit.script import Script

class Input:

    def __init__(self, data, transaction=None):
        self.transaction = transaction
        self.index = data.get('index', None)
        output = data['output']
        if isinstance(output, Output):
            self.output = output
        else:
            self.output = Output(output)

        self.signatures = []

        self._sig_hash = data.get('sig_hash', None)

    def native(self):
        tx_hex = self.output.transaction_hash
        txid = lx(tx_hex)
        vout = self.output.index
        outpoint = COutPoint(txid, vout)
        return CTxIn(outpoint)

    def sig_hash(self, redeem_script=None):
        return self.transaction.sig_hash(self, redeem_script)

class Output:

    def __init__(self, data, transaction=None):
        if transaction:
            self.transaction = transaction
        elif 'transaction_hash' in data:
            h = data['transaction_hash']
            #h = "".join(reversed(h))
            self._transaction_hash = h

        self.index = data.get('index', None)
        self.value = data.get('value', -1)
        self.address = data.get('address', None)
        self.metadata = data.get('metadata', {})

        if 'script' in data:
            # The dict here has two keys: 'type' and 'string'.
            # The Script class notices the 'string' key and parses
            # it to instantiate the native bitcoin.core.script.Cscript
            self.script = Script(**data['script'])
        else:
            self.script = None

    @property
    def transaction_hash(self):
        return self._transaction_hash or self.transaction.hash

    def native(self):
        return CTxOut(self.value, self.script.cscript)


class Transaction:


    def __init__(self, **options):
        self.inputs = []
        self.outputs = []
        if 'data' in options:
            self.set_data(options['data'])
        else:
            raise Exception("Invalid options")

    def set_data(self, data):
        self.version = data.get('version', 1)
        self.lock_time = data.get('lock_time', 0)
        self.hash = data.get('hash', None)

        for input_data in data.get('inputs', []):
            input_data['index'] = len(self.inputs)
            _input = Input(transaction=self, data=input_data)
            self.inputs.append(_input)

        for output_data in data.get('outputs', []):
            output = Output(transaction=self, data=output_data)
            self.outputs.append(output)

    def native(self):
        ins = [input.native() for input in self.inputs]
        outs = [output.native() for output in self.outputs]
        return CTransaction(ins, outs)


    def sig_hash(self, input, redeem_script=None):
        return SignatureHash(redeem_script.cscript, self.native(), input.index, SIGHASH_ALL)

    def serialize(self):
        return self.native().serialize()

    def to_hex(self):
        return hexlify(self.serialize())

    def txid(self):
        return Hash(self.serialize())

    def hex_hash(self):
        return b2lx(Hash(self.native().serialize()))

