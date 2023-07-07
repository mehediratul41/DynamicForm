import React, { useEffect, useMemo, useState } from 'react';
import { useTable, usePagination } from 'react-table';
import axios from 'axios';
import { Link, Outlet, useParams } from 'react-router-dom';

export const View = () => {
  const { tableName } = useParams();
  const [data, setData] = useState([]);

  useEffect(() => {
    // Fetch data from the API with the dynamic table name
    axios
      .get(`http://127.0.0.1:8000/${tableName.toLowerCase()}`)
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, [tableName]);

  const columns = useMemo(
    () => {
      if (data.length > 0) {
        return Object.keys(data[0]).map(key => ({
          Header: key,
          accessor: key
        }));
      }
      return [];
    },
    [data]
  );

  const tableInstance = useTable(
    {
      columns,
      data,
      initialState: { pageIndex: 0 }
    },
    usePagination
  );

  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    page,
    prepareRow,
    canPreviousPage,
    canNextPage,
    pageOptions,
    nextPage,
    previousPage,
    state: { pageIndex }
  } = tableInstance;

  return (
    <div>
        <h1>{tableName} Information</h1>
      <table {...getTableProps()} className="table">
        <thead>
          {headerGroups.map(headerGroup => (
            <tr {...headerGroup.getHeaderGroupProps()} className="table-header">
              {headerGroup.headers.map(column => (
                <th {...column.getHeaderProps()}>{column.render('Header')}</th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody {...getTableBodyProps()} className="table-body">
          {page.map((row, index) => {
            prepareRow(row);
            return (
              <tr {...row.getRowProps()} className="table-row">
                {row.cells.map(cell => (
                  <td {...cell.getCellProps()}>{cell.render('Cell')}</td>
                ))}
              </tr>
            );
          })}
        </tbody>
      </table>
      

      <div className="pagination">
        <button onClick={() => previousPage()} disabled={!canPreviousPage}>
          Previous
        </button>
        <span>
          Page{' '}
          <strong>
            {pageIndex + 1} of {pageOptions.length}
          </strong>
        </span>
        <button onClick={() => nextPage()} disabled={!canNextPage}>
          Next
        </button>
      </div>
    </div>
  );
};

export default View;






// import React, { useEffect, useMemo, useState } from 'react';
// import { useTable, usePagination } from 'react-table';
// import axios from 'axios';
// import { Link,Outlet,useParams } from 'react-router-dom';


// export const View = () => {
//     const { tableName } = useParams();
//     const [data, setData] = useState([]);
  
//     useEffect(() => {
//       // Fetch data from the API
//       fetch(`http://127.0.0.1:8000/${tableName}`)
//         .then(response => response.json())
//         .then(jsonData => {
//           // Convert the data into an array
//           const dataArray = Object.keys(jsonData).map(key => jsonData[key]);
//           setData(dataArray);
//         })
//         .catch(error => {
//           console.error('Error fetching data:', error);
//         });
//     }, []);
  
//     const columns = useMemo(
//       () => {
//         if (data.length > 0) {
//           return Object.keys(data[0]).map(key => ({
//             Header: key,
//             accessor: key
//           }));
//         }
//         return [];
//       },
//       [data]
//     );
  
//     const tableInstance = useTable(
//       {
//         columns,
//         data,
//         initialState: { pageIndex: 0 }
//       },
//       usePagination
//     );
  
//     const {
//       getTableProps,
//       getTableBodyProps,
//       headerGroups,
//       page,
//       prepareRow,
//       canPreviousPage,
//       canNextPage,
//       pageOptions,
//       nextPage,
//       previousPage,
//       state: { pageIndex }
//     } = tableInstance;
  
//     return (
//       <div>
//         <table {...getTableProps()} className="table">
//           <thead>
//             {headerGroups.map(headerGroup => (
//               <tr {...headerGroup.getHeaderGroupProps()} className="table-header">
//                 {headerGroup.headers.map(column => (
//                   <th {...column.getHeaderProps()}>{column.render('Header')}</th>
//                 ))}
//               </tr>
//             ))}
//           </thead>
//           <tbody {...getTableBodyProps()} className="table-body">
//             {page.map((row, index) => {
//               prepareRow(row);
//               return (
//                 <tr {...row.getRowProps()} className="table-row">
//                   {row.cells.map(cell => (
//                     <td {...cell.getCellProps()}>{cell.render('Cell')}</td>
//                   ))}
//                 </tr>
//               );
//             })}
//           </tbody>
//         </table>
  
//         <div className="pagination">
//           <button onClick={() => previousPage()} disabled={!canPreviousPage}>
//             Previous
//           </button>
//           <span>
//             Page{' '}
//             <strong>
//               {pageIndex + 1} of {pageOptions.length}
//             </strong>
//           </span>
//           <button onClick={() => nextPage()} disabled={!canNextPage}>
//             Next
//           </button>
//         </div>
//       </div>
//     );
//   };
  
//   export default View;