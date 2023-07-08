import React, { useEffect, useMemo, useState } from 'react';
import { useTable, usePagination } from 'react-table';
import axios from 'axios';
import { Link,Outlet } from 'react-router-dom';


export const Existing = () => {

  
  const styles = {
    color: 'white',
    padding: '10px',
    borderRadius: '5px',
    fontWeight: 'bold',
    textDecoration: 'capitalize',
  };

  const [formData, setFormData] = useState([]);
  const [selectedForm, setSelectedForm] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/formstructureformnames');
      const jsonData = await response.json();
      setFormData(jsonData);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };


  return (
    <div style={styles}>
      <h1>Forms</h1>
      <ol>
        {formData.map((item, index) => (
          <li className="formdata" key={index}>
           <span> {item.form_name}</span>
              <Link to={`/existing/view/${item.form_name}`}>
                <button>View</button>
             </Link>
             <Link to={`/existing/entry/${item.form_name}`}>
                 <button>Entry</button>
            </Link>
          </li>
        ))}
      </ol>

    </div>
  );
};

export default Existing;




//-----------------------------------------------------New code--------------------------------------

// import React, { useEffect, useMemo, useState } from 'react';
// import { useTable, usePagination } from 'react-table';
// import axios from 'axios';
// import { Link,Outlet } from 'react-router-dom';

// export function Existing() {

  // const styles = {
  //   color: 'white',
  //   padding: '10px',
  //   borderRadius: '5px',
  //   fontWeight: 'bold',
  //   textDecoration: 'capitalize',
  // };



//   const [tableNames, setTableNames] = useState([]);

//   useEffect(() => {
//     // Fetch table names from the FastAPI backend
//     axios.get('http://127.0.0.1:8000/formstructureformnames')
//       .then(response => {
//         setTableNames(response.data.table_names);
//       })
//       .catch(error => {
//         console.error(error);
//       });
//   }, []);

//   return (
//     <div style={styles}>
//       <h2>Table Names:</h2>
//       <ol >
//         {tableNames.map((tableName, index) => (
//           <li key={index}><h3>{tableName}</h3>
//            <div>
//               <Link to={`/existing/view/${tableName}`}>
//                 <button>View</button>
//               </Link>
//               <Link to={`/existing/entry/${tableName}`}>
//                 <button>Entry</button>
//               </Link>
//             </div>
//           </li>         
//         ))}
//       </ol>
//     </div>
//   );
// }

// export default Existing;


//-------------------------------------------------------------Old Table---------------------------------------------





//--------------------------------------------------------------------------Old Table-------------------------------------------------------------



//Old table

// import React, {useState, useEffect} from 'react'
// import axios from 'axios'


// export const Existing = () => {
//     const [data, setData] = useState([]);
  
//     useEffect(() => {
//       // Fetch data from the API
//       fetch('http://127.0.0.1:8000/food')
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
//     return (
//         <div>
//           <table>
//             <thead>
//               <tr>
//                 {data.length > 0 && Object.keys(data[0]).map(key => (
//                   <th key={key}>{key}</th>
//                 ))}
//               </tr>
//             </thead>
//             <tbody>
//               {data.map((row, index) => (
//                 <tr key={index}>
//                   {Object.values(row).map((value, index) => (
//                     <td key={index}>{value}</td>
//                   ))}
//                 </tr>
//               ))}
//             </tbody>
//           </table>
//         </div>
//       );
//     };
    
//     export default Existing;










// export const Existing = () => {
//     const [posts, setPosts] = useState([])

//     useEffect(() =>{
//         axios.get('http://127.0.0.1:8000/food/')
//             .then(res => {
//                 console.log(res)
//                 setPosts(res.data)
//             })
//             .catch(err => {
//                 console.log(err)
//             })
//     }, [])
//     return(
//         <div>
//             <table>
//             {posts.map(post =>(
//                     <tr key={post.id}><th>{post.name}</th></tr>
//                 ))}
//             </table>
//             <ul>
//                 {posts.map(post =>(
//                     <li key={post.id}>{post.name}</li>
//                 ))}
//             </ul>
//         </div>
//     )
// }