from typing import List, Union

from kb import Predicate, Substitution, Variable


class ForwardChainingEngine:
    def perform_query(self, facts: List[Predicate], q: Predicate) -> List[Substitution]:
        return [matchRes for fact in facts if (matchRes := self.match_fact(fact, q))]

    def match_fact(self, stored: Predicate, q: Predicate) -> Union[Substitution, None]:
        baseCheck = \
            stored.parsed["relation"] == q.parsed["relation"] \
            and len(stored.parsed["terms"]) == len(q.parsed["terms"])
        if not baseCheck:
            return None
        return self.match_terms(stored, q)

    def match_terms(self, stored: Predicate, query: Predicate) -> Union[Substitution, None]:
        acc = Substitution({})
        for i in range(len(stored.parsed["terms"])):
            stored_term = stored.parsed["terms"][i]
            query_term = query.parsed["terms"][i]
            if isinstance(query_term, Variable):
                acc.data[query_term.parsed] = stored_term
            elif query_term.parsed != stored_term.parsed:
                return None
        return acc
