### On the Limits of Byzantine-tolerant Spanning Tree Construction in Route-Restricted Overlay Networks Notes

## What are the contributions of this work?

1. Proof that self-stabilizing Byzantine leader election protocols for arbitrary network topologies inherently cannot ensure convergence to a global leader. Even without Byzantine nodes.

2. A self-stabliziing algorithm is presented for BFS spanning tree making use of cryptographic signatues to check the integrity of statements about hte distance to the root node. 

3. Results are presented from a simulation based on real-world data sets. Show that without cryptographic measures the spanning tree is highly vulnerable to attacks. 

## Notes:

* ID set is much larger than abs(V), where V is the set of all nodes in a network

# Node:
u = node
IDu = Node's ID
levelu = nodes level, non0negative interger variable
parentIDu = ID of parent node

# Solution to the BFS spanning tree problem

* gamma is a soltuion to the BFS spanning tree problem for a given leader, l in a subset of V with ID* , if every non-Byzantine process u fulfills the following conditions:

1. levelu = 0 iff IDu = ID*, leaders level is 0
2. levelu = Lmin + 1
3. parentIDu = IDu iff IDu = ID*, leaders parent ID is itself 
4. parentIDu is a subset of {IDv | v is a subset of N(u), levelv = Lmin(u)} iff IDu isnot ID*

V = a set of nodes in a network
E



## Algorithm, (puesdo lamen):



while true do:
	// For each neigbbor u, in Neighborhood N(u) do
	foreach i in N(u) do:
		// Read the input register from the neighbor u		
		lr_iu := read(r_iu)
	
	ts := getCurrentTime()

	if ID == ID* then:



## Definitions:

BFS = Breadth Frist Search, is an algorithm for tracering or searching tree or graph data structures. 

Attestation = Evidence or proof of something, a declaration that something exists or is the case

Hey Hoi, ik voel me een beetje in een moeilijke plek gezet. Aan het begin wou ik je graag binnen de familie welkomen en snapte dat je niet zo makkelijk is om meteen na Laura er bij te zijn. We hebben zeker paar goeie gesprekken gehad, en wel een band gevormd. Maar je blijft Thyco's vriendin, ik heb het idee dat je mij ook bleef appen om je zelf aftelijden van je studie en wanneer Thyco weg was om als nog de aandacht te krijgen van iemand die je van hem krijgt. Het werd misschien wel wat veel voor me. 

En om het lekker te luchten, vond ik het heel vervelend te zien hoe je met Thyco om ging na dat je de Auto wou hebben op de great ocean road. In mijn ogen wou je zelf iets, en in plaats van het zelf op te lossen ging je maar zeggen teggen Thyco dat die een vent moest zijn. Kwam een beetje over dat die maar blind voor je moest opkomen zonder dat er een plan of iets was, en dat neem ik je wel kwalijk. Thyco ken ik iemand die opkomt in waar die in gelooft, en is nooit bang geweest om zijn bek open te trekken. Door zo met Thyco om te gaan heb je het in mijn ogen een beetje verpest. 