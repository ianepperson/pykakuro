#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kakuro import Kakuro

one = Kakuro(4, (
     0 ,   0 ,(0,7),(0,6),
     0 ,(4,4),   1 ,   1 ,
  (7,0),   1 ,   1 ,   1 ,
  (6,0),   1 ,   1 ,   1 ,
))

two = Kakuro(5, (
       0 ,    0 ,(0,23),(0,21),     0,
       0 ,(8,15),    1 ,    1 ,     0,
    (8,0),    1 ,    1 ,    1 ,     0,
   (27,0),    1 ,    1 ,    1 ,     1,
    (5,0),    1 ,    1 ,    0 ,     0,
   (14,0),    1 ,    1 ,    0 ,     0,
       0 ,    0 ,    0 ,    0 ,     0,
))

three = Kakuro(8, (
      0 ,(0,23),( 0,30),      0 ,      0 ,( 0,27),( 0,12),( 0,16),
  (16,0),     1,     1 ,      0 , (24,17),     1 ,     1 ,     1,
  (17,0),     1,     1 , (29,15),      1 ,     1 ,     1 ,     1,
  (35,0),     1,     1 ,      1 ,      1 ,     1 ,( 0,12),     0,
  0     ,(7,0) ,     1 ,      1 , ( 8, 7),     1 ,     1 ,( 0, 7),
  0     ,(0,11),(16,10),      1 ,      1 ,     1 ,     1,      1,
  (21,0),     1,     1 ,      1 ,      1 ,( 5, 0),     1,      1,
  (6,0) ,     1,     1 ,      1 ,      0 ,( 3, 0),     1,      1,
))


four = Kakuro(8, (
  0,0,0,0,0,0,(0,16),(0,3),
  0,0,0,0,0,(8,6),1,1,
  0,(0,16),(0,6),0,(14,30),1,1,1,
  (11,0),1,1,(7,0),1,1,(0,6),0,
  (10,0),1,1,(13,7),1,1,1,(0,16),
  0,(14,0),1,1,1,(8,0),1,1,
  0,(0,4),(9,17),1,1,(11,0),1,1,
  (12,0),1,1,1,0,0,0,0,
  (10,0),1,1,0,0,0,0,0
))
