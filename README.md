Coursera Cryptography Course Scripts
=======================

These are the scripts I've used to solve Coursera Cryptography Course programming tasks.

#Week 1
A bunch of 10 cypher-text encrypted under the same key is provided. We have to decrypt another cypher-text. The idea is that if we exor two cypher-text we get the exor of the corresponding plain-texts. The combinations of two exored ASCII characters is quite limited and in particular when one of this characters is a white space the number of possibilities is reduced to one. The idea is to calculate the exor of every cypher-text combination and then we compare the obtained results.

For example if all the combinations of the message 1 with the other message get in position one a combination that is only possible with one space, we will know that in that particular position the message 1 has an space. In addition we know what letter is in that position in the other message by looking the possible ASCII characters combinations.

#Week 2
We have to implement CBC and CTR block cyphers.

#Week 3

#Week 4
We have to decrypt one cypher-text by applying a padding oracle attack. The basic idea consists in that a server replies with two different ways if the padding is not correct or the message is not correct.

#Week 5
We have to calculate the discrete log. of a particular big integer number. 

