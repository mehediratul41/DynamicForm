import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';


export const Entry = () => {
  const [formKeys, setFormKeys] = useState([]);
  const [formData, setFormData] = useState({});
  const [formId, setFormId] = useState('');
  const { tableName } = useParams();

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/formstructurekey/${tableName}`);
      const keys = response.data.keys.split(',').map(key => key.trim());
      setFormKeys(keys);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const handleInputChange = event => {
    const { name, value } = event.target;
    setFormData(prevFormData => ({ ...prevFormData, [name]: value }));
  };

  const handleFormIdChange = event => {
    setFormId(event.target.value);
  };

  const handleSubmit = async event => {
    event.preventDefault();
    try {
      const valuesString = Object.values(formData).join(', ');
      const requestBody = {
        form_id: formId,
        values: valuesString,
      };
      await axios.post('http://127.0.0.1:8000/formentry', requestBody);
      resetForm();
    } catch (error) {
      console.error('Error submitting data:', error);
    }
  };

  const resetForm = () => {
    setFormData({});
    setFormId('');
  };

  return (
    <div>
      <h2>{tableName} Entry</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="form_id">Form ID:</label>
          <input id="form_id" name="form_id" type="number" value={formId} onChange={handleFormIdChange} />
        </div>
        {formKeys.map(key => (
          <div key={key}>
            <label htmlFor={key}>{key}:</label>
            <input id={key} name={key} type="text" value={formData[key] || ''} onChange={handleInputChange} />
          </div>
        ))}
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default Entry;
