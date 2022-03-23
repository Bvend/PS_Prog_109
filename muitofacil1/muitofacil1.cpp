#include "Header.h"

float radianos_graus(float angulo)
{
	// Converte angulo para graus
	angulo = angulo * 180 / M_PI;
	// Retorna angulo arredondado de uma casa decimal
	return round(10 * angulo) / 10.0;
}