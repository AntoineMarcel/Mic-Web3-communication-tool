const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Mic", function () {
  it("Create NFT collection", async function () {
    const [owner, addr1] = await ethers.getSigners();

    const Mic = await ethers.getContractFactory("Mic");
    const mic = await Mic.deploy();
    await mic.deployed();
    await mic.awardItem(owner.address, "test.fr")

    expect(await mic.balanceOf(owner.address)).to.equal(1);
    await expect(mic.awardItem(owner.address, "test.fr")).to.be.revertedWith('Already have a Mic token');
  });
});
