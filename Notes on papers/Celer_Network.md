Definitions:

State Channel: State channels are a very broad and simple way to think about blockchain interactions which could occur on the blockchain, but instead get conducted off of the blockchain, without significantly increasing the risk of any participant. 

Sidechain Techniques: sidechain is a separate blockchain that is attached to its parent blockchain using a two-way peg. 

Congestion Gradients:

Celer Technology Stack:

Encompampasses a cleanly layered architecture that decouples sophisticated off-chain platform into hierarchical modules. 
Celer Network adopts off-chain technology stack that can be built on different blockchains, cStack

cStack:
cChannel: generalized state channel and sidechain suite
cRoute: provably optimal value transfer routings
cOS: development framework and runtime for off-chain enabled applications

cChannel:
Bottom of the stack, interacts with different underlying blockchains
Proves the upper-layer with a common abstraction of up-to-date states and bounded-time finality
Uses state channel (?) and side chain techniques (?)
Generic off-chain state transition:
Off-chain transactions can be arbitrary state transitions with dependency DAG.
Flexible and efficient value transfer:
Multiple state channel and sidechain constructions with different tradeoffs on efficiency and finality are provided to support fast value transfer with generic condition dependency, minimal on chain interactions and minimal fund lockup
Pure off-chain contract:
Any contract that is not directly associated with on0chain deposits does not need any on0chain operation or initialization unless a dispute is triggered.

cRoute:

Distributed Balanced Routing (DBR)
 Is proposed as an efficient routing protocol value transfers in an off-chain state channel network, inspired by the BackPressure routing Algorithm. DBR does not perform any explicit path computation from source to destination, instead routes direction by guided by  congestion gradients.

“Think of water flowing from the top of a hill
to a destination at the foot of the hill. The water does not need to know the route to
its destination; all it needs to do is to follow the direction of gravity”


Advantages:
Provably optimal throughput
“Given arrival rate of value transfer requests, if there exists any routing algorithm that “supports” the rate, DBR is also able to do that
Transparent channel balancing
Rebalancing process is naturally embedded in the routing process
Fully decentralized
Each node only needs to talk to its neighbours in the state channel network
Failure Resilience
Can quickly adapt and detect to unresponsive nodes
Privacy Preserving
Can seamlessly integrate with Onion routing
Multi-path nature the DBR is naturally preserve the privacy regarding the amount of transferred values. 

Protocol Description: 

Debt Queue:

Each node, i, maintains a debt queue for payments destined to each node k. 
Queue length is Qki (t), corresponds to the amount of tokens in the queue that should be relayed by node i to k at the beginning of slot t.



Channel Imbalance:

Congestion-plus-imbalance:



