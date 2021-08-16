#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

const unsigned UERROR = 65000;
const int maxint = 1000000;

typedef struct{
	unsigned j; // nodo
	int c; 		// atributo para expresar su peso, longitud, coste...
  } ElementoLista;

//vector de registros

typedef vector <ElementoLista> LA_nodo; //Se encarga de manipular y gestionar los datos

 
 class GRAFO {

	unsigned n; //Nº de nodos
	
	unsigned m; //Nº de aristas
	
	unsigned dirigido; // almacena 0 si el grafo es no dirigido, 1 eoc

	vector <LA_nodo> LS;	//Vector para la lista de sucesores y/o de adyacencia

	vector <LA_nodo> LP; //Vector para la lista de predecesores
	

  public:

	GRAFO(char nombrefichero[], int &errorapertura);

	void actualizar (char nombrefichero[], int &errorapertura);

	unsigned Es_dirigido(); //devuelve 0 si el grafo es no dirigido, 1 eoc

	void Info_Grafo();

	void Mostrar_Listas(int l);

	void ListaPredecesores();

	//Modificación 1 (Componentes conexas)

	void dfs (unsigned i, vector<bool> &visitado);

	void ComponentesConexas();

	~GRAFO();
};
