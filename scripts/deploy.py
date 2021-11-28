from brownie import accounts, HelloWorld


def deployHelloWorld():
    account = accounts[0]
    helloWorldObject = HelloWorld.deploy({"from": account})

    transaction = helloWorldObject.setName("Michael", {"from": account})
    transaction.wait(1)

    greeting = helloWorldObject.sayHello()


def main():
    deployHelloWorld()
