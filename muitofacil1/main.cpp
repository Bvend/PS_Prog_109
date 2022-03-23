#include "Header.h"

int main(void)
{
	float angulo;

	// Coleta angulo em radianos do usuário
	cout << "Digite um angulo em radianos" << endl;

	cin >> angulo;

	// Converte angulo para graus
	angulo = radianos_graus(angulo);

	// Imprime angulo convertido
	cout << angulo << endl;

	return 0;
}