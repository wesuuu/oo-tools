FROM wuykimpang/centos8-extended:latest

COPY . /opt/oo-tools

WORKDIR /opt/oo-tools

RUN python3 setup.py bdist_wheel
RUN pip3 install dist/*.whl
