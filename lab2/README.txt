- STEPS to use the algorithm:

1. Open the "bugtrk_in.csv" file and write 3 values in following order: number of cards, 
width of the cards, height of the cards.

2. Run the "runner.py" file to start the algorithm. 

3. Open the "bugtrk_out.csv" file to see the program result. The number in this file is
the minimun side length of the square. 



- EXPLANATION of the algorithm:

In the find_side_lenght() function the are 3 checks on the beginning to verify the type and
value of the input numbers.

The algorithm uses linked list (from the LinkedList class). Each node corresponds to a column
of cards on the desc, the value of each node is the number of cards in the column. 
The find_side_lenght() compares the total width and the total height is a new card was added,
and then puts the new card to the very bottom of the first column if the total height is
smaller then the total width, or puts the new card to an existing row if the total height is
greater then the total width.

The "index" variable point to a vacant place to put the card in order to fill all the existing
rows before adding a new card to the very bottom of the first column, creating a new row.