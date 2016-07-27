# tests
tests for interview for Providence Salumu from Morgan Stanley | Institutional Securities Tech

As discussed, you will find below a description of the problem I am trying to solve (thanks for helping out J). In the problem, we are looking at a program that can find a valid schedule for the Olympic games (Brazil, Rio 2016)
 
The outline of the problem is this :
·         The Olympic games run T parallel tracks, each track having the same number of sport slots, S; hence there are T*S sport slots in total. Assume that sport slots all start and finish at the same time across the tracks.

·         There are at most T*S sports to assign to tracks and slots (if there are fewer sports than slots, we can make up the difference with dummy sports that’d then represent empty slots).

·         There are a number of athletes who have each expressed which sport they’d like to compete in.

·         The goal is to assign sports to slots and tracks so that the athletes can attend all the sports they are qualified for; that is, we never schedule two sports that an athlete is qualified for on two different tracks in the same slot.

Below is an example. Support we have 2 tracks and 2 slots, and four sports named A, B, C and D. There are four atheletes – A1, A2, A3, A4 – and each is qualified to play 2 sports :
·         A1 is qualified to play in sports A and B

·         A2 is qualified to play in sports B and C

·         A3 is qualified to play in sports C and D

·         A4 is qualified to play in sports D and A

One solution to the above problem (there are many more):
Track #
Slot 1
Slot 2
1
B
C
2
D
A
 
Write a function that takes a list of atheletes, along with their sport qualifications, the maximum number of sport slots and the maximum number of tracks possible, and returns all the possible Olympic game schedules.
Create a github account (free for open source code) and share the code (python or C++, your convenience) on it please.
