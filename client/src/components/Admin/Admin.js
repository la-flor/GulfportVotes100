// import React, { useState } from 'react';
// import { useForm } from 'react-hook-form';
// import axios from 'axios';
// import './Admin.scss';

// const Admin = () => {
// 	const [form, setForm] = useState({ username: '', password: '' });

// 	const { register, handleSubmit, errors } = useForm();

// 	const handleForm = async () => {
// 		try {
// 			const response = await axios.post('http://localhost:5000/login', {
// 				username: form.username,
// 				password: form.password,
// 			});
// 		} catch (error) {
// 			console.log(error);
// 		}
// 	};

// 	const handleChange = (e) => {
// 		setForm({ ...form, [e.target.name]: e.target.value });
// 	};

// 	return (
// 		<div className='Login'>
// 			<div className='Login__Greeting'>
// 				<h4>Welcome,</h4>
// 				<p>Sign in to continue</p>
// 			</div>
// 			<form
// 				className='Login__Form'
// 				onSubmit={(e) => e.preventDefault()}
// 				autoComplete='on'>
// 				<label htmlFor='username' className='Login__Label'>
// 					Username
// 				</label>
// 				<input
// 					id='username'
// 					type='username'
// 					name='username'
// 					className='Login__Input'
// 					ref={register({
// 						required: true
// 					})}
// 					onChange={handleChange}
// 				/>
// 				{errors.username && <p className='Error'>• Username must be valid</p>}
// 				<label htmlFor='password' className='Login__Label'>
// 					Password
// 				</label>
// 				<input
// 					id='password'
// 					type='password'
// 					name='password'
// 					className='Login__Input'
// 					ref={register({
// 						required: '• You must specify a password',
// 						minLength: {
// 							value: 8,
// 							message: '• Password must have at least 8 characters',
// 						},
// 					})}
// 					onChange={handleChange}
// 				/>
// 				{errors.password && <p className='Error'>{errors.password.message}</p>}
// 				<button
// 					type='submit'
// 					className='Login__Submit'
// 					onClick={handleSubmit(handleForm)}>
// 					Submit
// 				</button>
// 			</form>
// 		</div>
// 	);
// };

// export default Admin;
