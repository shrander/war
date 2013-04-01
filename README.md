war
===

the card game 'War' 

Based on server client architecture.  

Server
======
Server will maintain game state
Server will read in commands from clients
Issue responses for those commands and modify the game state when an accepted command is given
In the response the server will identify how the client should proceed to the next game state

Client
======
Client will request moves and display view
The client has access to three "piles": arsenal, battlefield, and the spoils
arsenal - a stack of unplayed cards
battlefield - the game area where cards are overturned and the game is actually played
spoils - the pile of won cards

Protocol
========
The client will send request commands to the server: 
client.move([pile class], [pile class]) - client requests that the server move a card or cards from one pile to another
 response - if valid, server responds with a valid message.  If the move is from the arsenal pile to the battlefield
 pile, the server will also pass the battlefield state with the valid message.
client.confirm() - a confirmation that the player is ready to move to the next game state
