from csp import Constraint, CSP
from typing import Dict, List, Optional

class MapColoringConstraint(Constraint[str, str]):
    def __init__(self, place1: str, place2: str) -> None:
        super().__init__([place1, place2])
        self.place1: str = place1
        self.place2: str = place2
    
    def satisfied(self, assignment: Dict[str, str]) -> bool:
        # If either place is not in the assignment, then it is not
        # yet possible for their colors to be conflicting
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        # check the color assigned to place1 is not the same as the # color assigned to place2
        return assignment[self.place1] != assignment[self.place2]

class WhiteGlobalConstraint(Constraint):
    def __init__(self, place1: str, place2: str, place3: str, place4: str, place5: str, place6: str, place7: str, place8: str, place9: str) -> None:
        super().__init__([place1, place2, place2, place3, place4, place5, place6, place7, place8])

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        return not list(assignment.values()).count("white") >= 2

if __name__ == "__main__":
    variables: List[str] = ["BA", "MA", "PI", "CE", "RN", "PB", "PE", "AL", "SE"] 
    domains: Dict[str, List[str]] = {}
    for variable in variables:
        domains[variable] = ["red", "white", "green", "blue"]
    
    csp: CSP[str, str] = CSP(variables, domains)
    csp.add_constraint(WhiteGlobalConstraint("MA", "PI", "CE", "RN", "PB", "PE", "AL", "SE", "BA"))
    csp.add_constraint(MapColoringConstraint("MA", "PI"))
    csp.add_constraint(MapColoringConstraint("PI", "CE"))
    csp.add_constraint(MapColoringConstraint("PI", "PE"))
    csp.add_constraint(MapColoringConstraint("PI", "BA"))
    csp.add_constraint(MapColoringConstraint("CE", "RN"))
    csp.add_constraint(MapColoringConstraint("CE", "PB"))
    csp.add_constraint(MapColoringConstraint("CE", "PE"))
    csp.add_constraint(MapColoringConstraint("RN", "PB"))
    csp.add_constraint(MapColoringConstraint("PB", "PE"))
    csp.add_constraint(MapColoringConstraint("PE", "AL"))
    csp.add_constraint(MapColoringConstraint("PE", "BA"))
    csp.add_constraint(MapColoringConstraint("AL", "SE"))
    csp.add_constraint(MapColoringConstraint("AL", "BA"))
    csp.add_constraint(MapColoringConstraint("SE", "BA"))

solution: Optional[Dict[str, str]] = csp.backtracking_search()
if solution is None:
    print("No solution found!") 
else:
    print(solution)