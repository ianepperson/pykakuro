.. pykakuro documentation master file, created by
   sphinx-quickstart on Sat Apr  3 01:17:54 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pykakuro's documentation!
====================================

pykakuro is a set of python-based tools that can be used to generate and solve
(some) Kakuro puzzles.

.. warning::

  pykakuro has not had any offical releases yet. As such this documentation
  may be out-of-date or incomplete and the current version of the code may or
  may not work. Use at your own risk!

.. currentmodule:: kakuro

Generating puzzles
==================

Random puzzles of arbitrary size can be generated by calling this function:

.. autofunction:: new_puzzle

Puzzles are initially generated in the solved state. If you don't want to see
the solution you can *unsolve* the puzzle before printing it.::

  >>> puzzle = kakuro.new_puzzle(4,4,seed=10)
  >>> puzzle.unsolve()
  >>> print puzzle
   0  |0,11| 0  | 0  |
  ----+----+----+----+
  2,0 | 1  | 0  |0,8 |
  ----+----+----+----+
  9,0 | 1  |6,5 | 1  |
  ----+----+----+----+
   0  |7,0 | 1  | 1  |
  ----+----+----+----+

In this case, cells where a number belongs have a "1" and cells with no number
have a "0".

Due to the inherent difficulty of solving Kakuro puzzles, pykakuro is able to
generate puzzles much bigger than it can actually solve.

Solving puzzles
==================

Pykakuro can solve the puzzles it generates if they are not too big; just call
the solve method on the puzzle::

  >>> puzzle.solve()

Since puzzles generated by pykakuro are initially solved this is not too
interesting. You might be more interested to solving some already existing
puzzle.  Before you can do this you need to represent the puzzle in a form that
pykakuro understands.

Kakuro boards don't really lend themselves to being drawn in ASCII, but we'll
give it a shot. Here's a board the way you might see it drawn in a puzzle
book::

       |\ |\
       |7\|6\
    |\4|  |  |
    |4\|--+--+
  \7|  |  |  |
   \|--|--+--+
  \6|  |  |  |
   \|--+--+--+

To represent the board, we use a 0 for the cells that don't take a number and
a 1 for the cells that do. Constraint squares are a tuple of two integers,
with the first being the constraint ACROSS and the second being the
constraint DOWN. If no constraint is specified for a particular direction,
the integer should be 0. Here is the puzzle shown above in this format::

   0 | 0 |0,7|0,6|
  ---+---+---+---+
   0 |4,4| 1 | 1 |
  ---+---+---+---+
  7,0| 1 | 1 | 1 |
  ---+---+---+---+
  6,0| 1 | 1 | 1 |
  ---+---+---+---+

And here is the same puzzle encoded in the canonical format used by this
program::

  sample_puzzle = (0 ,   0 ,(0,7),(0,6),
                   0 ,(4,4),   1 ,   1 ,
                (7,0),   1 ,   1 ,   1 ,
                (6,0),   1 ,   1 ,   1 ,
                  )

Now that the puzzle is encoded correctly, the program can solve it::

  >>> result = kakuro.solve(sample_puzzle, 4)
  [0, 0, (0, 7), (0, 6), 0, (4, 4), 1, 3, (7, 0), 1, 4, 2, (6, 0), 3, 2, 1]

In the grid form, the solution looks like this::

  >>> print kakuro.pretty_print(result,4)
   0 | 0 |0,7|0,6|
  ---+---+---+---+
   0 |4,4| 1 | 3 |
  ---+---+---+---+
  7,0| 1 | 4 | 2 |
  ---+---+---+---+
  6,0| 3 | 2 | 1 |
  ---+---+---+---+

If you prefer the OO-approach, you can use the Kakuro object to accomplish the
same things.::

  >>> puzzle = kakuro.Kakuro(sample_puzzle, 4)
  >>> puzzle.solve()
  >>> print puzzle
   0 | 0 |0,7|0,6|
  ---+---+---+---+
   0 |4,4| 1 | 3 |
  ---+---+---+---+
  7,0| 1 | 4 | 2 |
  ---+---+---+---+
  6,0| 3 | 2 | 1 |
  ---+---+---+---+


Reference
=========

.. autoclass:: Kakuro

   .. automethod:: solve
   .. automethod:: check_puzzle
   .. automethod:: check_solution
   .. automethod:: unsolve

   .. attribute:: data

      Puzzle data.

      TODO: should be a descriptor so data changes can be detected

   .. note::

      The following properties are generally considered read-only and should
      not be changed after a puzzle is created unless you know what you're
      doing. No warnings are raised if they are modified, but the program's
      behavior may become undefined. If in doubt, create a new Kakuro object.

   .. attribute:: x_size

      Width of puzzle. (We assume all puzzles are square)

   .. attribute:: difficulty

      A floating point value indicating the anticipated difficulty of this
      puzzle for a human to solve. It is scaled such that 0.01 is "Very easy"
      and 1.0 is "Extremely difficult", however values greater than 1.0 are
      possible.

      Note that the puzzle must have been previously solved with .solve() in
      order for this value to have been calculated. Otherwise, attempting to
      access it will raise an AttributeError.

      TODO: make this a property and lazily calculate this value

   .. attribute:: min_val

      Minimum value allowed in solutions (normally 1)

   .. attribute:: max_val

      Maximum value allowed in solutions (normally 9)

   .. attribute:: is_exclusive

      True if numbers following clues must be exclusive, False if they can be
      repeated. (ie "2,2,2" would be allowed for the clue 6 if this was False)

   .. attribute:: is_solved

      True if the puzzle is considered solved by the tool (by creating a random
      solved puzzle or by calling .solve() on any puzzle), False if it is
      considered unsolved.

   .. attribute:: num_entry_squares

      Total number of entry squares in this puzzle.

   .. attribute:: search_space_size

      Total number of possible puzzle states. This is equal to
      :math:`(\text{max\_val}-\text{min\_val} +
      1)^{\text{num\_entry\_squares}}`.
      Except for small puzzles this number will be very large making
      brute-force searches of the entire space intractable.

   .. attribute:: brute_force_size

      Number of puzzle states that must be explored using the brute force
      algorithm in order to solve the puzzle.

      Note that the puzzle must have been previously solved with .solve() in
      order for this value to have been calculated. Otherwise, attempting to
      access it will raise an AttributeError.

      TODO: make this a property and lazily calculate this value

.. toctree::
   :maxdepth: 2

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

