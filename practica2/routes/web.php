<?php

use Illuminate\Support\Facades\Route;

use App\Http\Controllers\diarioController;

Route::get('/', [diarioController::class,'metodoInicio'])->name('apodoInicio');
Route::get('/formulario', [diarioController::class,'metodoFormulario'])->name('apodoFormulario');
Route::get('/recuerdos', [diarioController::class,'metodoRecuerdos'])->name('apodoRecuerdos');

Route::post('/guardarRecuerdo', [diarioController::class,'metodoGuardar'])->name('guardarFormulario');


/*
Route::controller(diarioController::class)->group(function (){
    Route::get('/','metodoInicio')->name('apodoInicio');
    Route::get('/formulario','metodoFormulario')->name('apodoFormulario');
    Route::get('/recuerdos','metodoRecuerdos')->name('apodoRecuerdos');

});
*/



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

/*Route::get('/', function () {
    return view('welcome');
});*/

/*
 El primer parametro es el nombre de la ruta y el segundo parametro es el nombre del archivo

    Route::view('/','inicio')->name('rutaInicio');
    Route::view('/vista1','vista1')->name('rutavista1');
    Route::get('/vista2', function () {
        return view('vista2');
    });
    Route::get('/vista3', function () {
        return view('vista3');
    });

*/