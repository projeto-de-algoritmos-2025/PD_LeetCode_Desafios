'''
300. Longest Increasing Subsequence: https://leetcode.com/problems/longest-increasing-subsequence/description/
Exercício resolvido por Ester Flores e Eduardo Schuindt.
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Calcula o comprimento da Maior Subsequência Crescente (LIS) em O(n^2) usando Programação Dinâmica.
        PD[i] = Comprimento do LIS que TERMINA em nums[i].
        """
        n = len(nums)
        if n == 0:
            return 0

        # Inicializa a tabela PD. Cada elemento é um LIS de comprimento 1 (o próprio elemento).
        pd = [1] * n
        max_lis_length = 0

        # Itera por cada elemento para calcular seu PD[i]
        for i in range(n):
            # Compara nums[i] com todos os elementos anteriores
            for j in range(i):
                # Se nums[i] pode estender o LIS que termina em nums[j]
                if nums[i] > nums[j]:
                    # Atualiza pd[i] com o maior LIS possível + 1 (o próprio nums[i])
                    pd[i] = max(pd[i], pd[j] + 1)
            
            # Rastreamos o comprimento máximo encontrado até agora
            max_lis_length = max(max_lis_length, pd[i])

        return max_lis_length
        