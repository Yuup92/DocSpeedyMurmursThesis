Definitions:

Payment channel networks: is a blockchain transaction that escrows a given user money in order to enable future transaction to a specific recipient, much like a gift card. 

Head of line blocking: large transactions can block shorter payments that could have been serviced quickly. 

Maximum transaction unit (MTU): max unit value that a transaction can have over a network.

Payment Channel:

Funds can be transferred repeatedly and securely without recording every transaction to the blockchain. Allowing for faster and more payments to happen without appending the transactions to the blockchains ledger. Increasing throughput

First proposed payment channel: Lighting Network
Other proposed payment channels: SpeedyMurmurs, Bitcoin;s lightning Network, Ethereum’s Raiden Network, Spider Network

Design problems: are much like communication networks. 

They require efficient mechanisms to find paths with enough capacity for payments, high throughput and low delay. 
Efficient networking is essential to the economic viability of payment channel networks
The network design must provide the right economic incentives to both end-users and service providers that route payments 
The network should ensure the privacy of user transactions.
Payment channels may become imbalanced and will limit transaction throughput over a certain channel

Spider Network:

Packet-switched payment channel network, that breaks up payments into transaction units
Spider hosts send payments over the network by transmitting a series of transaction units, analogous to packets in a data network. Each transaction unit transfers an amount of money bounded by the maximum transaction unit (MTU). Transaction units from different payments are queued at Spider routers, which transmit them as funds become available in payment channels. 

Design features: 
Uses congestion control
in-network scheduling mechanisms to achieve high utilization and best-effort payment delivery within a deadline. 
Payments are not done atomically, like that of other payment channel services.
Key facet: imbalance-aware routing

Work based on:
Multipath transport protocols like MPTCP
Stability of end-to-end algorithms for joint routing and rate control. ACM SIGCOMM Computer Communication Review
Joint congestion control, routing, and mac for stability and fairness in wireless networks. IEEE Journal on Selected Areas in Communications

Results:
For a given amount of funds locked into the network: 
Spider is able to complete 10-75% more transactions amounting to a 10-45% increase in volume of transactions relative to SpeedyMurmurs and SilentWhispers 
On an ISP-like topology:
outperforms a classical max-flow based-approach by 5-15% on both the number and volume of successful transactions.


Spider Hosts:

Transport Interface: 
Allows for both atomic and non-atomic payments
Congestion control

Atomic Payments: 
A guaranty that an atomic payment is fully delivered or no payment takes place
Uses: Atomic Multi-Path Payments (AMP)

Non-Atomic Payment: 
The transport of payment is allowed to partially or fully deliver the payment. 
If payment is not fully delivered the sender may try again on a later time or complete the transaction on the blockchain transaction

Congestion Control:
Congestion control is used to determine the rate to send transaction units for different payments
Outside of scope of paper
No real explanation how this works


Spider Routers:

Responsible for forwarding transaction units to the intended receiver, makes use of some vague sort of Onion routing to ensure privacy
Queues transaction units if it does not have the funds to send them, waits for payments to come from ‘other side’ to send queued payments. 
Queuing payments results in increased delays for some payments
May be possible to prioritize payments based on size, deadline or routing fees. 

Routing (read the next sections)??





