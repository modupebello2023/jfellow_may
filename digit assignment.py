{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6d76787f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LETTERS: 50\n",
      "DIGITS: 5\n"
     ]
    }
   ],
   "source": [
    "def count_letters_and_digits(sentence):\n",
    "    no_of_letter = 0\n",
    "    no_of_digits = 0\n",
    "    index = 0\n",
    "    \n",
    "    while index < len(sentence):\n",
    "        c = sentence[index]\n",
    "        if c.isalpha():\n",
    "            no_of_letter += 1\n",
    "        elif c.isdigit():\n",
    "            no_of_digits += 1\n",
    "        index += 1\n",
    "    \n",
    "    return no_of_letter, no_of_digits\n",
    "\n",
    "sentence = \"Jifunz is an amazing bootcamp and thanks to all the team over 12345\"\n",
    "no_of_letter, no_of_digits = count_letters_and_digits(sentence)\n",
    "print(\"LETTERS:\", no_of_letter)\n",
    "print(\"DIGITS:\", no_of_digits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b10ad79d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
