
#include "grafo.h"

using namespace std;

int componente_conexa = 0; //Lo utilizaremos para contar el nº de componentes conexas que hay

      GRAFO::GRAFO(char nombrefichero[], int &errorapertura){
	     int i;
         int j;
         ifstream grafo(nombrefichero); //empieza a leer fichero
         if(grafo.fail()) errorapertura = 1;//comprobar si hay error
         grafo >> n >> m >> dirigido;
         LS.resize(n);//le da al vector LS(lista de sucesores) el tama�o que indica el archivo(n�mero de nodos)
            for(int count = 1; count <= m; count++)
            {
               grafo >> i >> j;
               ElementoLista dummy;
               dummy.j = j-1;
	      	   LS[i-1].push_back(dummy);//carga cada elemento en el vector LS

               if(!Es_dirigido())//si no es dirigido, usamos LS como adyacencias y no usamos LP
               {
               ElementoLista dummy2;
               dummy2.j = i-1;
               LS[j-1].push_back(dummy2);
               }
               
            else {ListaPredecesores();}//si es dirigido, se llama al m�todo para la lista de predecesores
	}
      }

      void GRAFO::actualizar (char nombrefichero[], int &errorapertura){//libera memoria lista y carga nuevo grafo desde fichero.
      
         for(int i = 0; i < n; i++){   //libera
            
            LS[i].clear();
            if (Es_dirigido()) LP[i].clear();

         }

         LS.clear();
         LP.clear();

         int i;
         int j;

         ifstream grafo(nombrefichero);
         if(grafo.fail())errorapertura = 1;//repetimos la carga de grafo
         grafo >> n >> m >> dirigido;
         LS.resize(n);
         

         for(int count = 1; count <= m; count++){

            grafo >> i >> j;
            ElementoLista dummy;
            dummy.j = j-1;
	         LS[i-1].push_back(dummy);
	        
            if(!Es_dirigido()){

               ElementoLista dummy2;
               dummy2.j = i-1;
               LS[j-1].push_back(dummy2);
            }
         
         }

         if(Es_dirigido()){

            ListaPredecesores();
         } 

      }

      unsigned GRAFO::Es_dirigido()//comprueba si es dirigido
      {
         if(dirigido==1){
            return 1;
         }else return 0;
      }

      void GRAFO::Info_Grafo() //indica si el grafo es o no dirigido y el numero de arcos/aristas
      {
         if(Es_dirigido())  cout << "Grafo dirigido"    << " | nodos " << n << " | arcos "   << m << endl;
         if(!Es_dirigido()) cout << "Grafo no dirigido" << " | nodos " << n << " | aristas " << m << endl;
      }

      void GRAFO::Mostrar_Listas(int l){

         if(l==0){ //muestra LS
      

		      if (Es_dirigido()){
                cout << "Nodos de la lista de sucesores: " << endl;
            }

		      else{

               cout << "Nodos de la lista de adyacentes: " << endl;
            } 	
             
		cout<< LS.size() <<endl;
		cout<< LS[8].size() <<endl;		
            for(int i = 0; i < n; i++){//escribe los nodos
            
               int aux = i + 1;
               int size = LS[i].size();

               cout << "[" << aux << "] : ";

               for(int k = 0; k < size; k++){

                  int aux = LS[i][k].j;
                  aux+= 1;
                  cout << aux ;
                  if(k!=size-1) cout <<  " | ";
               }

               if(LS[i].size() == 0) cout<< "null";
               cout << endl;
            }
         }else if (l==1) //muestra LP
         {
            cout << "Nodos de la lista de predecesores" << endl;

            for(int i = 0; i < n; i++){//escribe los nodos
            
               int aux = i + 1;
               int size = LP[i].size();
               cout << "[" << aux << "] : ";
               for(int k = 0; k < size; k++)
               {
                  int aux = LP[i][k].j;
                  aux+= 1;
                  cout << aux ;
                  if(k!=size-1) cout <<  " | ";
               }
               if(LP[i].size() == 0) cout<< "null";
               cout << endl;
            }
         }
      }

      void GRAFO::ListaPredecesores() //m�todo de predecesores
      {
          LP.resize(n);
            for(int i = 0; i < n; i++)
            {
               int size = LS[i].size();
               for(int k = 0; k < size; k++)
               {
                  ElementoLista dummy;
                  dummy.j = LS[i][k].j;
                  ElementoLista dummy2;
                  dummy2.j = i;
                  LP[dummy.j].push_back(dummy2);
               }  
            }
      }
      	
	void GRAFO::dfs(unsigned i, vector<bool> &visitado) {  
	
	
		visitado[i] = true;  //Lo marcamos como true (como que el nodo i ha sido visitado)   
		cout << i+1 << ", ";  
		
		for (unsigned j=0;j<LS[i].size();j++){ //Recorremos la componente conexa (subgrafo)

			if (visitado[LS[i][j].j] == false){ //Si el nodo eseno esta visitado entonces lo recorremos en profundidad
			 	dfs(LS[i][j].j, visitado); //Recorrido en profundidad	
			 } 
		}            	                  
	} 

	void GRAFO::ComponentesConexas(){
	
		vector<bool> visitado;  //Vamos a utilizar un vector "visitado" en formato booleano (true false)
		
		visitado.resize(n);  //Redimencionamos en vector visitado pasandole el nº de nodos que tiene nuestro grafo

    	for( int i = 0; i < n ; i++ ){   
			visitado[i] = false;
		}
		

    	for(int i = 0; i < n ; i++ ){    //Recorremos todos los nodos
    			 
         	if( visitado[ i ] == false){          //Si algun nodo no ha sido visitado, habrá una componente conexa
             	cout<<"\n Componente Conexa: "<<componente_conexa + 1; //Imprimo los nodos de cada componente 
             	cout<<" {  " ;
             	
            	dfs(i,visitado);  //Lamamos al dfs para que realice el recorrido en profundidad
            	
             	cout<<" }";
             	cout<<"\n\n";
             	
             	componente_conexa++;                   // Incrementamos el nº de componentes conexas
           	}
    	}	
			cout<<"\n Cantidad de Componentes Conexas es: "<<componente_conexa<<endl;	
	}
      
      GRAFO::~GRAFO(void) //destructor
      {
         for(int i = 0; i < n; i++){
            LS[i].clear();
            LP[i].clear();
         }
         LS.clear();
         LP.clear();
      }
      
    

