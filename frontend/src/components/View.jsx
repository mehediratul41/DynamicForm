import React, { useEffect, useMemo, useState } from 'react';
import { useTable, usePagination } from 'react-table';
import axios from 'axios';
import { Link, Outlet, useParams } from 'react-router-dom';

export const View = () => {
  const styles = {
    color: 'white',
    padding: '10px',
    borderRadius: '5px',
    fontWeight: 'bold',
    textDecoration: 'capitalize',
  };


  const [tableData, setTableData] = useState([]);
  const [tableKeys, setTableKeys] = useState([]);
  const { tableName } = useParams();


  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response1 = await axios.get(`http://127.0.0.1:8000/formstructurekeyandformid/${tableName}`);
      const form_id = response1.data.form_id;
      const response2 = await axios.get(`http://127.0.0.1:8000/formentry/${form_id}`);
      
      const keys = response1.data.keys.split(',').map(key => key.trim());
      const values = response2.data.map(item => item.values.split(','));

      setTableKeys(keys);
      setTableData(values);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const data = useMemo(
    () =>
      tableData.map((row, index) =>
        tableKeys.reduce(
          (acc, key, columnIndex) => ({
            ...acc,
            [`value${columnIndex}`]: row[columnIndex],
          }),
          {}
        )
      ),
    [tableData, tableKeys]
  );

  const columns = useMemo(
    () =>
      tableKeys.map((key, index) => ({
        Header: key,
        accessor: `value${index}`,
      })),
    [tableKeys]
  );

  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    prepareRow,
    page,
    canPreviousPage,
    canNextPage,
    pageOptions,
    nextPage,
    previousPage,
    gotoPage,
    pageCount,
    state: { pageIndex },
  } = useTable(
    {
      columns,
      data,
      initialState: { pageIndex: 0 },
    },
    usePagination
  );

  return (
    <div style={styles}>
      <h2>{tableName} Information</h2>
      <table className='tablestyle' {...getTableProps()} style={{ width: '100%' }}>
        <thead>
          {headerGroups.map(headerGroup => (
            <tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map(column => (
                <th {...column.getHeaderProps()}>{column.render('Header')}</th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody {...getTableBodyProps()}>
          {page.map((row, rowIndex) => {
            prepareRow(row);
            return (
              <tr {...row.getRowProps()}>
                {row.cells.map((cell, cellIndex) => (
                  <td {...cell.getCellProps()}>{cell.render('Cell')}</td>
                ))}
              </tr>
            );
          })}
        </tbody>
      </table>
      <div className='paginate'>
        <button onClick={() => gotoPage(0)} disabled={!canPreviousPage}>
          {'<<'}
        </button>
        <button onClick={() => previousPage()} disabled={!canPreviousPage}>
          {'<'}
        </button>
        <button onClick={() => nextPage()} disabled={!canNextPage}>
          {'>'}
        </button>
        <button onClick={() => gotoPage(pageCount - 1)} disabled={!canNextPage}>
          {'>>'}
        </button>
        <span>
          Page{' '}
          <strong>
            {pageIndex + 1} of {pageOptions.length}
          </strong>{' '}
        </span>
      </div>
    </div>
  );
};

export default View;

