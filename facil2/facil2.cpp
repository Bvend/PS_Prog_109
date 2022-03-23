#include "Header.h"

int conta_uns(int num)
{
	// Inicia contagem do n�mero de uns em 0
	int p = 1;
	int num_uns = 0;

	// Encontra menor pot�ncia de dois maior do que n�mero informado
	while (p < num)
	{
		p *= 2;
	}

	// Subtrai do n�mero informado a maior pot�ncia de dois menor do que o n�mero, at� esse ser zero
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