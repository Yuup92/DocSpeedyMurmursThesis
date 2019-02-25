# What is your research area and why is it important?

% reference the white paper of bitcoin
% reference the difference in speed between cc and crypto

10 years ago Bitcoin was introduced as a decentralized digital currency, since then the monetary system has seen a rise and fall in value. Different implementations of Bitcoin, cryptocurrencies, have entered the market trying to solve different issues with Bitcoin and extend cryptocurrencies use cases. As the cryptocurrency technology matures, different inherent issue with cryptocurrencies are tying to be solved. The amount of transactions that can be processed by Bitcoin is in the order of 10,000 times slower than that of credit-card solutions for transactions. 

One solution to the problem of slow transaction rates is to make use of payment channels and bundle transactions. Payment channels allow a pair or group of users to exchange currency without having to push every transaction to the blockchain, this is done by having a start transaction that records all the balance of each channel and by a end transaction that records the final state of each channel. Using this technique allows for a series of transactions to take place without having to push each one onto the blockchain. Allowing for a higher throughput of currency exchange than if every transaction needed to be pushed to the blockchain. 

The idea of payment channels has become an increasingly interesting topic for the past ?? years, as different solutions come to the market, e.g. lightning for Bitcon, Raiden for Ethereum, etc. As this relatively new technology emerges onto the market, different problems still need to be solved. As of now the transaction load on payment channel networks is relatively low. As payment channels technology matures so will the load on the network, this brings forth interesting research topics. For example how to deal with concurrency in the network for payments. How will the network handle multiple payments being requested at the same time, how is the routing done? Who gets priority and how can it be ensured that the throughput of the network is still possible.

#What is the concrete problem you want to solve?

The problem that is being addressed in this research is how one deals with concurrency in a payment channel network. As the load of the payment channel networks increase how should the network handle when payment requests come in at the same time? Simulating concurrency for a payment channel network will allow for an in-depth analysis of how concurrency is currently implemented in SpeedyMurmurs. With the concurrency analysis different strategies can be examined to deal with concurrency and implemented so that the payment channel network will be able to function under a heavier load. 

#Why is it important in the context of the research area?

Concurrency within payment channel networks while not a new concept, is a field of research with limited amount of research mainly investigating how payment channel networks deal with concurrency. Due to the relatively new concept of payment channels overlayed on a cryptocurrency network, researching how these networks will work under higher workload will allow for the technology to grow and stay ahead of the implementation and usuage. Due to the workload of payment channels being relatively low at the moment. 

#How do you want to solve the problem ?

To tackle the problem of concurrency observation in a payment channel overlay a simulation will be created to simulate how an actual network may work. The analysis will be done on real data-sets and simulated data-sets. Seeing as all current work on actual data does not comprise of enough concurrent communication between exchanges. 

#How do you want to evaluate that your solution is good? (Also: why is the problem challenging and an actual research problem, not just implementation)

To evaluate if the concurrency implementations are actual solutions to the problem, some base-line simulations will need to be made with no changes to the speedy murmur code. Then the base-line simulation will be compared to the changed concurrency handling of the algorithm. Throughput, volume and time delay will all be used to measure and compare.

#What is your initial time plan?

To finish it on time.

