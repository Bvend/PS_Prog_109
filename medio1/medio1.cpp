#include "Header.h"

double distancia(double coord_x1, double coord_y1, double coord_x2, double coord_y2)
{
	// Calcula distância entre dois pontos em um plano cartesiano e retorna valor encontrado
	return sqrt((coord_x2 - coord_x1) * (coord_x2 - coord_x1) + (coord_y2 - coord_y1) * (coord_y2 - coord_y1));
}