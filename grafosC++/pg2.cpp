#include "grafo.cpp"

using namespace std;
	
	char fichero[100];
	int error;
	char letra;
	
int main(void){
	
	system(" cls ");
	cout<<"Introduce el nombre completo del fichero de datos"<<endl;
	cin >> fichero;
	GRAFO OBJETO_GRAFO(fichero, error);
	system(" cls ");

	while(1){

		cout<<"\n\tActividad I, Optimiza!cion: carga basica de un grafo"<<endl;
		cout<<"\tc. [c]argar grafo desde fichero"<<endl;
		cout<<"\ti. Mostrar [i]nformacion basica del grafo"<<endl;
		
		if(OBJETO_GRAFO.Es_dirigido()){
			cout<<"\ts. Mostrar lista de [s]ucesores del grafo"<<endl;
			cout<<"\tp. Mostrar lista de [p]redecesores del grafo"<<endl;
		}
		
		else{	
			cout<<"\ta. Mostrar lista de [a]dyacencias del grafo"<<endl;
		}
		
		cout<<"\to. Mostrar lista de c[o]mponentes conexas del grafo"<<endl;

		cout<<"\tIntroduce la opcion a ejecutar > ";
		cin>>letra;


	switch(letra){

		case 'c':

			system(" cls ");

			cout<<"Introduce el nombre completo del fichero de datos"<<endl;
			OBJETO_GRAFO.actualizar(fichero,error);
			
			if(error==0){
				cout<<"Fichero cargado correctamente"<<endl;
			}
				
		break;

		case 'i':

			system(" cls ");

			OBJETO_GRAFO.Info_Grafo();
			
		break;

		case 's':

			system(" cls ");

				if(OBJETO_GRAFO.Es_dirigido()){
					OBJETO_GRAFO.Mostrar_Listas(0);
				}

				else{
					cout<<"No existe tal lista en el grafo actual"<<endl;
				}
			
		break;

		case 'p':

			system(" cls ");

			if(OBJETO_GRAFO.Es_dirigido()){
				OBJETO_GRAFO.Mostrar_Listas(1);
			}

			else{
				cout<<"No existe tal lista en el grafo actual"<<endl;
			}
		
		break;
			
		case 'a':

			system(" cls ");

			if(OBJETO_GRAFO.Es_dirigido()){
				cout<<"No existe tal lista en el grafo actual"<<endl;
			}

			else{
				OBJETO_GRAFO.Mostrar_Listas(0);
			}
			
		break;
		
		case 'o':

			system(" cls ");
			
			OBJETO_GRAFO.ComponentesConexas();
			
			if(componente_conexa >= 2){
				cout<<"\n El grafo es no conexo."<<endl;
			}
			
			else{
				cout<<"\n El grafo es conexo."<<endl;
			}
			
		break;
		
		case 'q':

			system(" cls ");
			
			exit (-1);
		
		break;
		
		default:
		
		break;
		}
	}
	
	return 0;
}
