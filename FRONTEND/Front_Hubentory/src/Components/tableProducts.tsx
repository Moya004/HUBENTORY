import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../Components/stylestable.css';
import img_filter from '../assets/filter.png';

interface Item {
  id: number;
  id_prod: string;
  id_inv: string;
  id_cate: string;
  lote: string;
  name: string;
  quantity: number;
  caduco: string;
}

const DataTable: React.FC = () => {
  const [data, setData] = useState<Item[]>([]);
  const [searchTerm, setSearchTerm] = useState<string>('');
  const [filter, setFilter] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedItems, setSelectedItems] = useState<number[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get<Item[]>('URL_DE_TU_API');
        setData(response.data);
      } catch (error) {
        setError('Error al obtener los datos');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const handleSearch = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchTerm(event.target.value);
  };

  const handleFilterChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setFilter(event.target.value);
  };

  const handleCheckboxChange = (id: number) => {
    setSelectedItems((prevSelectedItems) =>
      prevSelectedItems.includes(id)
        ? prevSelectedItems.filter((item) => item !== id)
        : [...prevSelectedItems, id]
    );
  };

  const filteredData = Array.isArray(data)
    ? data.filter((item: Item) =>
        (searchTerm === '' || 
          item.id_prod.toLowerCase().includes(searchTerm.toLowerCase()) ||
          item.id_inv.toLowerCase().includes(searchTerm.toLowerCase()) ||
          item.id_cate.toLowerCase().includes(searchTerm.toLowerCase()) ||
          item.lote.toLowerCase().includes(searchTerm.toLowerCase()) ||
          item.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
          item.quantity.toString().includes(searchTerm) ||
          item.caduco.toString().includes(searchTerm)) &&
        (filter === '' || item.id_cate === filter || item.lote === filter)
      )
    : [];

  return (
    <div className="data-table-container">
      <div className="filters">
        <input
          type="text"
          placeholder="Buscar..."
          value={searchTerm}
          onChange={handleSearch}
        />

        <img src={img_filter} />
        <select className='boxfilter' value={filter} onChange={handleFilterChange}>
          <option  value="">Elige una opcion</option>
          <optgroup label="Categorías">
            {/* Aquí puedes mapear las categorías disponibles */}
            <option value="Categoría A">Categoría A</option>
            <option value="Categoría B">Categoría B</option>
            <option value="Categoría C">Categoría C</option>
          </optgroup>
          <optgroup label="Lotes">
            {/* Aquí puedes mapear los lotes disponibles */}
            <option value="Lote 1">Lote 1</option>
            <option value="Lote 2">Lote 2</option>
            <option value="Lote 3">Lote 3</option>
          </optgroup>
        </select>
      </div>
      {loading ? (
        <p>Cargando datos...</p>
      ) : error ? (
        <p>{error}</p>
      ) : (
        <table className="data-table">
          <thead>
            <tr>
              <th></th>
              <th>ID Producto</th>
              <th>ID Inventario</th>
              <th>ID Categoria</th>
              <th>Lote</th>
              <th>Nombre</th>
              <th>Existencias</th>
              <th>Caduco</th>
            </tr>
          </thead>
          <tbody>
            {filteredData.length > 0 ? (
              filteredData.map((item: Item) => (
                <tr key={item.id}>
                  <td>
                    <input
                      type="checkbox"
                      checked={selectedItems.includes(item.id)}
                      onChange={() => handleCheckboxChange(item.id)}
                    />
                  </td>
                  <td>{item.id_prod}</td>
                  <td>{item.id_inv}</td>
                  <td>{item.id_cate}</td>
                  <td>{item.lote}</td>
                  <td>{item.name}</td>
                  <td>{item.quantity}</td>
                  <td>{item.caduco}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan={8}>No se encontraron datos</td>
              </tr>
            )}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default DataTable;
