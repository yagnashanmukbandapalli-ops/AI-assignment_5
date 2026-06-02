# AI Assignment 5 - README

## PROJECT 1: SEARCH TECHNIQUES

### 1. minimax.py

* Demonstrates the Minimax algorithm
* Applied to Tic-Tac-Toe gameplay
* Determines the best possible move

### 2. alphabeta.py

* Demonstrates Alpha-Beta Pruning
* Eliminates unnecessary search branches
* Enhances execution performance

### 3. heuristic_alphabeta.py

* Demonstrates Heuristic Alpha-Beta Search
* Uses a heuristic evaluation function
* Effective for larger state spaces

### 4. monte_carlo.py

* Demonstrates Monte Carlo Tree Search (MCTS)
* Utilizes the UCT (Upper Confidence Bound for Trees) formula
* Widely applied in AI game-playing systems

### Execution Commands

```bash
python minimax.py
python alphabeta.py
python heuristic_alphabeta.py
python monte_carlo.py
```

## PROJECT 2: AI TRAVEL RECOMMENDATION SYSTEM

### planner.py

#### Main Features

* Suggests tourist attractions according to user interests
* Takes the available budget into account
* Uses a basic knowledge-based dataset

#### Sample Input

City: Hyderabad

Interest: Historical

Budget: 3000

#### Expected Output

Suggested tourist destinations that fit the specified budget.

### Execution Command

```bash
python planner.py
```

## PROJECT 3: KNOWLEDGE GRAPH

### knowledge_graph.txt

Stores sample knowledge graph triples consisting of:

* Entity
* Relation
* Attribute

### Technologies Studied

* Neo4j
* Apache Jena
* Protégé
* RDFLib

## PROJECT 4: BAYESIAN NETWORK

### bayesian_model.py

#### Library Used

* pgmpy

#### Example Network

Rain → Traffic → Late

#### Purpose

Performs probabilistic reasoning and inference using Bayesian Networks.

### Installation

```bash
pip install pgmpy
```

### Execution Command

```bash
python bayesian_model.py
```

## TESTING

### Alpha-Beta Pruning

* Analyze and compare the number of explored nodes.

### Heuristic Alpha-Beta

* Execute with search depths 2, 4, and 6.

### Monte Carlo Tree Search

* Run with varying numbers of iterations.

## REPORT CONTENTS

The report should include:

* Description of algorithms
* Flowcharts
* Output screenshots
* Time and space complexity analysis
* Advantages and limitations
* Real-world applications
