<?php
namespace App\Http\Controllers;


use Illuminate\Foundation\Http\FormRequest;

class validarFormDiario extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     */
    public function authorize(): bool
    {
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, \Illuminate\Contracts\Validation\ValidationRule|array<mixed>|string>
     */
    public function rules(): array
    {
        return [
            //Reglas de validacion en el controlador
            'txtTitulo' => 'required|max:10',
            'txtRecuerdos' => 'required|min:5',
        ];
    }
}