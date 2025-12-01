'''
1092. Shortest Common Supersequence: https://leetcode.com/problems/shortest-common-supersequence/description/
Exercício resolvido utilizando Alinhamento de Sequências (LCS) e Backtracking.
Exercício resolvido por Ester Flores e Eduardo Schuindt.
'''

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        Encontra a menor supersequência comum construindo a tabela de alinhamento
        e recuperando a sequência ótima (similar ao algoritmo Find_Sequence).
        """
        n, m = len(str1), len(str2)
        
        # Construção da Tabela (Sequence Alignment) 
        # Usa lógica de LCS: Match ganha ponto, Mismatch propaga o máximo.
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if str1[i] == str2[j]:
                    # Caso 1: Match 
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    # Caso 2: Gap/Mismatch
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        # Recuperação da Sequência (Algoritmo Find_Sequence)
        # Realiza o backtracking da célula (n, m) até (0, 0)
        res = []
        i, j = n, m

        while i > 0 and j > 0:
            # Se caracteres são iguais, fazem parte da LCS
            if str1[i - 1] == str2[j - 1]:
                res.append(str1[i - 1])
                i -= 1
                j -= 1
            # Se não, move na direção que deu o valor ótimo 
            elif dp[i - 1][j] > dp[i][j - 1]:
                # Veio de cima: significa que str1[i-1] não estava na LCS, então adicionamos ele
                res.append(str1[i - 1])
                i -= 1
            else:
                # Veio da esquerda: significa que str2[j-1] não estava na LCS, adicionamos ele
                res.append(str2[j - 1])
                j -= 1

        # Adiciona os caracteres restantes 
        while i > 0:
            res.append(str1[i - 1])
            i -= 1
        while j > 0:
            res.append(str2[j - 1])
            j -= 1

        # A sequência foi construída de trás para frente
        return "".join(res[::-1])