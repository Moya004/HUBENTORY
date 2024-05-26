import React, { useState, useEffect } from 'react';
import axios from 'axios';
import img_filter from '../assets/filter.png';

interface Item {
  id: number;
  fecha: string;
  autor: string;
  detalles: string;
}

const DataTable: React.FC = () => {
  const [data, setData] = useState<Item[]>([]);
  const [searchTerm, setSearchTerm] = useState<string>('');
  const [filter, setFilter] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedItems, setSelectedItems] = useState<number[]>([]);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [itemsPerPage] = useState<number>(15);

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
          item.id.toString().includes(searchTerm) ||
          item.fecha.toLowerCase().includes(searchTerm.toLowerCase()) ||
          item.autor.toLowerCase().includes(searchTerm.toLowerCase()) ||
          item.detalles.toLowerCase().includes(searchTerm.toLowerCase())) &&
        (filter === '' || item.id.toString() === filter)
      )
    : [];

    
  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentItems = filteredData.slice(indexOfFirstItem, indexOfLastItem);

  // Calcular el total de páginas
  const totalPages = Math.ceil(filteredData.length / itemsPerPage);

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
          {/* Aquí puedes mapear las opciones disponibles */}
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
              <th>ID</th>
              <th>Fecha</th>
              <th>Autor</th>
              <th>Detalles</th>
            </tr>
          </thead>
          <tbody>
              {currentItems.length > 0 ? (
                currentItems.map((item: Item) => (
                  <tr key={item.id}>
                    <td>
                      <input
                        type="checkbox"
                        checked={selectedItems.includes(item.id)}
                        onChange={() => handleCheckboxChange(item.id)}
                      />
                    </td>
                    <td>{item.id}</td>
                    <td>{item.fecha}</td>
                    <td>{item.autor}</td>
                    <td>{item.detalles}</td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan={5}>No se encontraron datos</td>
                </tr>
              )}
            </tbody>
        </table>
      )}
      <div className='container-btnpage'>
        <span>{currentPage} / {totalPages}</span>
        <button className='btnprevius' onClick={() => setCurrentPage(currentPage - 1)} disabled={currentPage === 1}></button>
        <button className='btnext' onClick={() => setCurrentPage(currentPage + 1)} disabled={currentPage === totalPages}></button>
      </div>
    </div>
  );
};

export default DataTable;
