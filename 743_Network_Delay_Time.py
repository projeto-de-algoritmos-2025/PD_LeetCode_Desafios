'''
743. Network Delay Time: https://leetcode.com/problems/network-delay-time/description/
Exercício resolvido utilizando o algoritmo de Bellman-Ford.
Exercício resolvido por Ester Flores e Eduardo Schuindt.
'''

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Calcula o tempo mínimo para o sinal atingir todos os nós.
        Aplica o relaxamento de arestas N-1 vezes.
        """
        # Inicialização
        # M[v] é inicializado com infinito para todos os nós, exceto a fonte k.
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        
        # Rodamos o loop n-1 vezes. 
        for i in range(n - 1):
            changed = False  
            
            for u, v, w in times:
                # Se a origem u já foi alcançada e encontramos um caminho mais curto para v
                # Recorrência: M[v] > M[u] + C_uv 
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    changed = True
            
            # Se nenhum valor mudou nesta iteração, podemos parar cedo 
            if not changed:
                break
        
        # O resultado é o tempo máximo entre os caminhos mínimos calculados, pois o sinal precisa chegar a TODOS os nós.
        max_dist = 0
        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                return -1 # Um nó inalcançável significa que o sinal não chegou a todos.
            max_dist = max(max_dist, dist[i])
            
        return max_dist