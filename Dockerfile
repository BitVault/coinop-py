FROM ubuntu
RUN apt-get -y install gcc make libpython-all-dev libffi-dev python-pip
RUN pip install PyNaCl
RUN mkdir coinop-py
ADD ./coinop ./coinop-py/coinop
ADD ./coinop.egg-info ./coinop-py/coinop.egg-info
ADD ./setup.py ./coinop-py/setup.py
RUN cd ./coinop-py && python setup.py install
CMD cd ./coinop-py && py.test
