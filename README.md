# Harmony Web3 Example
 Simple python script that shows how to connect to the harmony blockchain and read HRC20 token balances

#create virtual environment
virtualenv harmony

#start virtual environment
source harmony/bin/activate


#install pyhmy
https://github.com/harmony-one/pyhmy

#install pyhmy
pip install pyhmy

#libraries needed to compile pyhmy
#install go
sudo apt install golang-go
#install libraries
sudo apt install libgmp-dev  libssl-dev  make gcc g++

#cd to pyhmy git folder and compile
make install

#web3
pip install web3