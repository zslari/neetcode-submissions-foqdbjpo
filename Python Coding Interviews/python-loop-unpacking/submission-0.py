from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:

    max_score = 0
    top_scorer = None
    
    for score in scores:
        name, result = score[0], score[1]
        if result > max_score:
            max_score = result
            top_scorer = name
        
    return top_scorer
        



# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
