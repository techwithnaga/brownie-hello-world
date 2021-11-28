//SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract HelloWorld {
    string name = "John Doe";

    function setName(string memory _name) public {
        name = _name;
    }

    function getName() public view returns (string memory) {
        return name;
    }

    function sayHello() public view returns (string memory) {
        return
            string(
                abi.encodePacked("Hello World, from Brownie! My name is ", name)
            );
    }
}
