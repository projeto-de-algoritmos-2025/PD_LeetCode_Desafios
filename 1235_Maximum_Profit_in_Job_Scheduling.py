'''
1235. Maximum Profit in Job Scheduling: https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/
Exercício resolvido por Ester Flores e Eduardo Schuindt.
'''

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        Calcula o lucro máximo possível ao agendar tarefas sem sobreposição, usando PD e Busca Binária (O(n log n)).
        
        :param startTime: Lista com os horários de início das tarefas.
        :param endTime: Lista com os horários de término das tarefas.
        :param profit: Lista com os lucros de cada tarefa.
        :return: O lucro máximo.
        """
        
        n = len(startTime)
        
        # 1. Pré-processamento: Combinar (endTime, startTime, profit) e ordenar pelo tempo de término.
        jobs = sorted(zip(endTime, startTime, profit))
        
        # end_times é usado para a Busca Binária: contém apenas os tempos de término ordenados.
        end_times = [job[0] for job in jobs]
        
        # pd[i] armazena o lucro máximo obtido usando um subconjunto dos primeiros i+1 trabalhos.
        pd = [0] * n
        
        # 2. Iteração e Transição de PD (Bottom-Up)
        for i in range(n):
            current_end, current_start, current_profit = jobs[i]
            
            # Opção A: Excluir o Trabalho 'i'
            # Lucro = Lucro máximo obtido até o trabalho anterior (i-1).
            profit_excluding = pd[i - 1] if i > 0 else 0
            
            # Opção B: Incluir o Trabalho 'i'. Encontra o índice 'j' do *último* trabalho que termina antes ou em current_start.
            # bisect_right retorna o ponto de inserção para manter a ordem.
            # A subtração por 1 garante que estamos olhando para o último trabalho compatível.
            j = bisect.bisect_right(end_times, current_start) - 1
            
            # profit_from_previous_compatible: Lucro máximo obtido até o índice j.
            # Se j >= 0, usamos dp[j]. Caso contrário (j < 0), o lucro é 0.
            profit_from_previous_compatible = pd[j] if j >= 0 else 0
            
            profit_including = current_profit + profit_from_previous_compatible
            
            # 3. Escolha Ótima: Máximo entre incluir e excluir o trabalho 'i'.
            pd[i] = max(profit_excluding, profit_including)
            
        # 4. Resultado Final. O resultado é o lucro máximo após considerar todos os trabalhos.
        return pd[n - 1]