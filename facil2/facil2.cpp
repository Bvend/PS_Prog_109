#include "Header.h"

int conta_uns(int num)
{
	// Inicia contagem do número de uns em 0
	int p = 1;
	int num_uns = 0;

	// Encontra menor potência de dois maior do que número informado
	while (p < num)
	{
		p *= 2;
	}

	// Subtrai do número informado a maior potência de dois menor do que o número, até esse ser zero
	while (num > 0)
	{
		while (p > num)
		{
			p /= 2;
		}
		num -= p;
		num_uns++;
	}
	
	// Retorna uns contabilizados
	return num_uns;
}