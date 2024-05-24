import React, { useState } from 'react';
import '../Components/stylestable.css';

const DataTable: React.FC = () => {
  // Datos de ejemplo
  const [data] = useState<any[]>([
    { id: 1, name: 'Elemento 1', category: 'Categoría A', quantity: 10 },
    { id: 2, name: 'Elemento 2', category: 'Categoría B', quantity: 15 },
    { id: 3, name: 'Elemento 3', category: 'Categoría A', quantity: 8 },
    { id: 4, name: 'Elemento 4', category: 'Categoría C', quantity: 20 },
  ]);

  // Estado para el filtro de búsqueda
  const [searchTerm, setSearchTerm] = useState<string>('');

  // Función para manejar el cambio en el campo de búsqueda
  const handleSearch = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchTerm(event.target.value);
  };

  // Función para filtrar los elementos según el término de búsqueda
  const filteredData = data.filter((item: any) =>
    item.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    item.category.toLowerCase().includes(searchTerm.toLowerCase()) ||
    item.quantity.toString().includes(searchTerm)
  );

  return (
    <div className="data-table-container">
      <input
        type="text"
        placeholder="Buscar..."
        value={searchTerm}
        onChange={handleSearch}
      />
      <table className="data-table">
        <thead>
          <tr>
            <th>Seleccionar</th>
            <th>Nombre</th>
            <th>Categoría</th>
            <th>Cantidad</th>
          </tr>
        </thead>
        <tbody>
          {filteredData.map((item: any) => (
            <tr key={item.id}>
              <td><input type="checkbox" /></td>
              <td>{item.name}</td>
              <td>{item.category}</td>
              <td>{item.quantity}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DataTable;
