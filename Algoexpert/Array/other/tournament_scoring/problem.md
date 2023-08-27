## Tournmatent Scoring
### Problem Statement

In a tournament, _n_ teams play against each other exactly once. Each game results in either one of the two teams winning. There are no ties. The winner of a particular game receives _3_ points, and the loser receives _0_ points. It is guaranteed that the total score of each team is unique.
write a function that takes in a list of pairs representing the teams that have competed against each other and an array containing the results of each competition, and returns the winner of the tournament. The input array contains elements in the form of `[homeTeam, awayTeam]`and the results array contains information about the winner of each corresponding game in the input array. Specifically, `results[i]` denotes the winner of `competitions[i]`, where `1` in the `results` array means that the home team in the corresponding competition won and `0` means that the away team won.
If each team have only one win(each team has _3_ points), Then return the frist winner in the input array.

### Sample Input
```python
competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"],
]
results = [0, 0, 1]
```

### Sample Output
```python
"Python"
```

### Solution pseudocode
```text
1. create a dictionary to store the teams and their scores
2. iterate through the competitions array
3. if the result is 1, add 3 points to the home team
4. if the result is 0, add 3 points to the away team
5. return the team with the highest score
```
