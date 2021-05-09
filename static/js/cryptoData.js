//  Authors:                                Sandro Aguilar
//  Date:                                   May 8, 2021
//  Class:                                  CS 361
//  Description:                            This JS file is used to hold data on
//                                          crypto assets that will be listed.

// -------------------------------------------------------------------------

const cryptoNames = ["Bitcoin", "Ethereum", "Litecoin", "Dai", "USDT", "Chainlink", "Uniswap", "PancakeSwap", "Pancake Bunny", "BNB"];
const cryptoData = {
  bitcoin:{name: "Bitcoin", image: "/static/img/btc.png", supply: 18696643},
  ethereum: {name: "Ethereum", image: "/static/img/eth.png", supply: 0},
  litecoin: {name: "Litecoin", image: "/static/img/ltc.png", supply: 0},
  dai: {name: "Dai", image: "/static/img/dai.png", supply: 0},
  usdt: {name: "USDT", image: "/static/img/usdt.png", supply: 0},
  chainlink: {name: "Chainlink", image: "/static/img/link.png", supply: 0},
  uniswap: {name: "Uniswap", image: "/static/img/uni.png", supply: 0},
  pancakeswap: {name: "Pancake Swap", image: "/static/img/cake.png", supply: 0},
  pancakebunny: {name: "Pancake Bunny", image: "/static/img/bunny.png", supply: 0},
  bnb: {name: "", image: "/static/img/bnb.png", supply: 0}
}