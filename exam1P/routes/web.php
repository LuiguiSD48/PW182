<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/
/*
Route::get('/', function () {
    return view('welcome');
});
*/

Route::view('/', 'inicio');
Route::view('/vista1', 'vista1');
Route::get('/vista2', function () {
    return view('vista2');
});
Route::get('/vista3', function () {
    return view('vista3');
});