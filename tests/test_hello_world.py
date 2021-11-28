from brownie import HelloWorld, accounts


def testGetDefaultName():
    # Arrange
    account = accounts[0]

    # Action
    helloWorldObject = HelloWorld.deploy({"from": account})

    # Assert
    assert helloWorldObject.getName() == "John Doe"


def testChangeName():
    # Arrange
    account = accounts[0]

    # Action
    helloWorldObject = HelloWorld.deploy({"from": account})
    transaction = helloWorldObject.setName("Naga", {"from": account})

    # Assert
    expected = "Naga"
    assert expected == helloWorldObject.getName()


def testSayHello():
    # Arrange
    account = accounts[0]

    # Action
    HelloWorldObject = HelloWorld.deploy({"from": account})
    transaction = HelloWorldObject.setName("Naga", {"from": account})
    transaction.wait(1)

    # Assert
    expected = "Hello World, from Brownie! My name is Naga"
    assert expected == HelloWorldObject.sayHello()
