{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Function Demonstration\n",
    "\n",
    "# define a function to print items in a list\n",
    "# (make sure function is documented)\n",
    "def print_list(list_variable):\n",
    "    \"\"\"Prints items in a list \n",
    "\n",
    "        input:\n",
    "        ======\n",
    "\n",
    "            list_variable : a list-like object (can be used in a for loop)\n",
    "        \n",
    "        output:\n",
    "        =======\n",
    "\n",
    "            Each item in the list is printed; nothing is returned\n",
    "    \"\"\"\n",
    "\n",
    "\n",
    "    # loop over the list/ iterate over the list variable\n",
    "    for var in list_variable:\n",
    "\n",
    "        # print each item\n",
    "        print(var)\n",
    "\n",
    "# return (exit the function)\n",
    "    return\n",
    "\n",
    "\n",
    "\n",
    "# define some lists\n",
    "list1 = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0,] \n",
    "list2 = [\"a\", \"string\", \"whatever\",\"dum\"]\n",
    "\n",
    "# use that funtion to print some lists\n",
    "\n",
    "print_list(list1)\n",
    "print_list(list2)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
