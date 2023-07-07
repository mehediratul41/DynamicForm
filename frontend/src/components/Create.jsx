import React, { useState } from 'react';
import axios from 'axios';

export const Create = () => {
  const [formId, setFormId] = useState(0);
  const [formName, setFormName] = useState('');
  const [keys, setKeys] = useState('');
  const [types, setTypes] = useState('');

  const handleFormIdChange = event => {
    setFormId(Number(event.target.value));
  };

  const handleFormNameChange = event => {
    setFormName(event.target.value);
  };

  const handleKeysChange = event => {
    setKeys(event.target.value);
  };

  const handleTypesChange = event => {
    setTypes(event.target.value);
  };

  const handleSubmit = async event => {
    event.preventDefault();

    // Validation
    if (isNaN(formId)) {
      console.error('Form ID must be an integer.');
      return;
    }

    if (typeof formName !== 'string' || formName.trim() === '') {
      console.error('Form Name must be a non-empty string.');
      return;
    }

    if (typeof keys !== 'string' || keys.trim() === '') {
      console.error('Keys must be a non-empty string.');
      return;
    }

    if (typeof types !== 'string' || types.trim() === '') {
      console.error('Types must be a non-empty string.');
      return;
    }

    const requestBody = {
      form_id: formId,
      form_name: formName,
      keys,
      types,
    };

    try {
      await axios.post('http://127.0.0.1:8000/formstructure', requestBody);
      // Handle successful submission (e.g., show success message, redirect, etc.)
      console.log('Form submitted successfully!');
    } catch (error) {
      console.error('Error submitting form:', error);
    }
  };

  return (
    <div>
      <h1>Create Form</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="form_id">Form ID:</label>
          <input id="form_id" name="form_id" type="number" value={formId} onChange={handleFormIdChange} required />
        </div>
        <div>
          <label htmlFor="form_name">Form Name:</label>
          <input id="form_name" name="form_name" type="text" value={formName} onChange={handleFormNameChange} required />
        </div>
        <div>
          <label htmlFor="keys">Keys:</label>
          <input id="keys" name="keys" type="text" value={keys} onChange={handleKeysChange} required />
        </div>
        <div>
          <label htmlFor="types">Types:</label>
          <input id="types" name="types" type="text" value={types} onChange={handleTypesChange} required />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default Create;
