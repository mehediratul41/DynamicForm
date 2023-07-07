import React, { useState, useEffect } from 'react';
import { useForm } from 'react-hook-form';
import { useParams } from 'react-router-dom';
import axios from 'axios';

export const Entry = () => {
  const styles = {
    color: 'Red',
    padding: '10px',
    borderRadius: '5px',
    fontWeight: 'bold',
    textDecoration: 'capitalize',
  };

  const { tableName } = useParams();
  const { register, handleSubmit } = useForm();
  const [columnValues, setColumnValues] = useState([]);

  useEffect(() => {
    fetchColumnValuesFromDatabase(tableName)
      .then((data) => {
        console.log('Fetched column values:', data);
        setColumnValues(data);
      })
      .catch((error) => {
        console.error('Error fetching column values:', error);
      });
  }, [tableName]);

  const fetchColumnValuesFromDatabase = async (tableName) => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/column_names/${tableName}`);
      const valuesArray = Object.values(response.data); // Convert response JSON object values to an array
      return valuesArray || [];
    } catch (error) {
      throw error;
    }
  };

  const onSubmit = (data) => {
    console.log('Form data:', data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {columnValues.map((nestedArray, index) => (
        <div key={index}>
          {nestedArray.map((value, nestedIndex) => (
            <div style={styles} key={nestedIndex}>
              <label style={styles} htmlFor={`input-${index}-${nestedIndex}`}>{value}</label>
              <input
                type="text"
                id={`input-${index}-${nestedIndex}`}
                name={`input-${index}-${nestedIndex}`}
                {...register(`input-${index}-${nestedIndex}`)}
              />
            </div>
          ))}
        </div>
      ))}
      <button type="submit">Submit</button>
    </form>
  );
};

export default Entry;



// --------------------------------------------------Ready code Old without nested array --------------------------------------------------


// import React, { useState, useEffect } from 'react';
// import { useForm } from 'react-hook-form';
// import { useParams } from 'react-router-dom';
// import axios from 'axios';

// export const Entry = () => {

//     const styles = {
//         color: 'Red',
//         padding: '10px',
//         borderRadius: '5px',
//         fontWeight: 'bold',
//         textDecoration: 'capitalize',
//       };

//   const { tableName } = useParams();
//   const { register, handleSubmit } = useForm();
//   const [columnNames, setColumnNames] = useState([]);

//   useEffect(() => {
//     fetchColumnNamesFromDatabase(tableName)
//       .then((data) => {
//         console.log('Fetched column names:', data);
//         setColumnNames(data);
//       })
//       .catch((error) => {
//         console.error('Error fetching column names:', error);
//       });
//   }, [tableName]);

//   const fetchColumnNamesFromDatabase = async (tableName) => {
//     try {
//       const response = await axios.get(`http://127.0.0.1:8000/column_names/food`);
//       const columnNames = Object.keys(response.data); // Assuming the response is an object with column names as keys
//       return columnNames || [];
//     } catch (error) {
//       throw error;
//     }
//   };

//   const onSubmit = (data) => {
//     console.log('Form data:', data);
//   };

//   return (
//     <form onSubmit={handleSubmit(onSubmit)}>
//       {columnNames.map((columnName) => (
//         <div style={styles} key={columnName}>
//           <label style={styles} htmlFor={columnName}>{columnName}</label>
//           <input type="text" id={columnName} name={columnName} {...register(columnName)} />
//         </div>
//       ))}
//       <button type="submit">Submit</button>
//     </form>
//   );
// };

// export default Entry;




// --------------------------------------------------Ready code  without nested array--------------------------------------------------







