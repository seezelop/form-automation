import React, { useState } from "react";
import { Button, Form, Card } from "react-bootstrap";
import axios from "axios";

const FormularioCorreo = () => {
  const [correo, setCorreo] = useState('');
  const [asunto, setAsunto] = useState('');
  const [mensaje, setMensaje] = useState('');
  const [archivo, setArchivo] = useState(null);
  const [errores, setErrores] = useState({}); // Para validaciones

  const validarCampo = (id, value) => {
    let error = '';
    switch (id) {
      case 'correo':
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
          error = 'Formato de correo inválido.';
        }
        break;
      case 'asunto':
        if (value.trim().length === 0) {
          error = 'El asunto no puede estar vacío.';
        }
        break;
      case 'mensaje':
        if (value.trim().length === 0) {
          error = 'El mensaje no puede estar vacío.';
        }
        break;
      default:
        break;
    }
    return error;
  };

  const handleInputChange = (e) => {
    const { id, value } = e.target;
    const error = validarCampo(id, value);
    setErrores((prevState) => ({
      ...prevState,
      [id]: error,
    }));

    if (id === 'correo') setCorreo(value);
    else if (id === 'asunto') setAsunto(value);
    else if (id === 'mensaje') setMensaje(value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('correo', correo);
    formData.append('asunto', asunto);
    formData.append('mensaje', mensaje);
    formData.append('archivo', archivo);

    try {
      const response = await axios.post('http://localhost:5000/enviar', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      
      if (response.data.status === 'success') {
        alert('Correo enviado correctamente.');
      }
    } catch (error) {
      console.error('Error al enviar el correo:', error);
      alert('Error al enviar el correo.');
    }
  };

  return (
    <div className="container d-flex justify-content-center align-items-center min-vh-100">
      <Card className="p-4" style={{ width: '100%', maxWidth: '600px' }}>
        <h2 className="text-center mb-4">Formulario de Envío de Correo</h2>
        <Form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label htmlFor="correo" className="form-label">Correo destinatario</label>
            <Form.Control
              type="email"
              id="correo"
              value={correo}
              onChange={handleInputChange}
              isInvalid={!!errores['correo']}
            />
            <Form.Control.Feedback type="invalid">
              {errores['correo']}
            </Form.Control.Feedback>
          </div>
          
          <div className="mb-3">
            <label htmlFor="asunto" className="form-label">Asunto</label>
            <Form.Control
              type="text"
              id="asunto"
              value={asunto}
              onChange={handleInputChange}
              isInvalid={!!errores['asunto']}
            />
            <Form.Control.Feedback type="invalid">
              {errores['asunto']}
            </Form.Control.Feedback>
          </div>

          <div className="mb-3">
            <label htmlFor="mensaje" className="form-label">Mensaje</label>
            <Form.Control
              as="textarea"
              id="mensaje"
              value={mensaje}
              onChange={handleInputChange}
              isInvalid={!!errores['mensaje']}
            />
            <Form.Control.Feedback type="invalid">
              {errores['mensaje']}
            </Form.Control.Feedback>
          </div>

          <div className="mb-3">
            <label htmlFor="archivo" className="form-label">Archivo adjunto</label>
            <Form.Control
              type="file"
              id="archivo"
              onChange={(e) => setArchivo(e.target.files[0])}
            />
          </div>

          <Button type="submit" className="w-100" variant="primary">
            Enviar Correo
          </Button>
        </Form>
      </Card>
    </div>
  );
};

export default FormularioCorreo;
