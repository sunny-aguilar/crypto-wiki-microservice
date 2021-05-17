//  Authors:                                Sandro Aguilar
//  Date:                                   May 8, 2021
//  Class:                                  CS 361
//  Description:                            This JS file is used to hold data on
//                                          crypto assets that will be listed.

// -------------------------------------------------------------------------

const cryptoNames = ["Bitcoin", "Ethereum", "Litecoin", "Dai", "USDT", "Chainlink", "Uniswap", "PancakeSwap", "Pancake Bunny", "BNB"];

const cryptoSummaries = {
  Polygon: "With polygon, any project can easily spin-up a dedicated blockchain network which combines the best features of stand-alone blockchains (sovereignty, scalability and flexibility) and Ethereum (security, interoperability and developer experience). Additionally, these blockchains are compatible with all the existing Ethereum tools (Metamask, MyCrypto, Remix etc), and can exchange messages among themselves and with Ethereum.Decentralized Apps are making huge progress but the current blockchain ecosystem is not prepared to scale as per the demand. The issues of slow block confirmations and high gas fees need to be solved before we target mass adoption by mainstream users. And most importantly, it needs awesome user experience. We aim to change that by simplifying the interaction between users and the decentralized world. We want to make interacting with the decentralized ecosystem so easy that anyone can do so without worrying about the complexity of the system.",
  Pancakeswap: "PancakeSwap is an automated market maker (AMM) — a decentralized finance (DeFi) application that allows users to exchange tokens, providing liquidity via farming and earning fees in return. It launched in September 2020 and is a decentralized exchange for swapping BEP20 tokens on Binance Smart Chain. PancakeSwap uses an automated market maker model where users trade against a liquidity pool. These pools are filled by users who deposit their funds into the pool and receive liquidity provider (LP) tokens in return. These tokens can later be used to reclaim their share of the pool, as well as a portion of the trading fees. These LP tokens are known as FLIP. PancakeSwap also allows users to farm additional tokens such as CAKE and SYRUP. On the farm, users can deposit LP tokens and get rewarded with CAKE. PancakeSwap allows users to trade BEP20 tokens, provide liquidity to the exchange and earn fees, stake LP tokens to earn CAKE, stake CAKE to earn more CAKE and stake CAKE to earn tokens of other projects.",
  BNB: "Binance Coin is the cryptocurrency issued by Binance exchange and trades with the BNB symbol. Binance coin initially ran on the Ethereum blockchain with ERC 20 standard but has since become the native coin of the Binance chain. Binance coin has a strict maximum of 200 million BNB tokens. Every quarter, Binance uses one-fifth of its profits to repurchase and permanently destroy, or 'burn,' Binance coins held in its treasury. Binance was created as a utility token for discounted trading fees in 2017, but its uses have expanded to numerous applications, including payments for transaction fees (on the Binance Chain), travel bookings, entertainment, online services, and financial services."
};

// export functions
export { cryptoSummaries };