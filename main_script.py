"""This is the main script
"""
import sys
import os
import numpy as na
import scipy as sp
import matplotlib.pyplot as plt
import directory_names as dn
import dipole_moment as dp
import energy_extract as en
import elastic_strain as stn
import avs2vtkr_conv as may
import energy_extract_nn3 as en3
import make2Dslice as sl
import images2gif as gif
import cProfile
import pstats
import StringIO
import getpass
if getpass.getuser() == 'dominique':
    if 'Scripts' not in 'sys.path':
        sys.path.append(os.path.relpath('.'))

# pylint: disable=C0303
# pylint: disable=R0912
# pylint: disable=R0914
# pylint: disable=R0915


def main():
    """The main function
        usage: make_dep.py -oNew [angle start (deg) ]\
         [angle end (deg) ] [ no of angles ]
    """
    print 'this is make_dep.py\n\n'
    # Why is this import now working
    # from the top level?
    import states2transition as st
    # DEFINING COMMON STRINGS
    prefix = dn.prefix
    suffix = 'output'
    # NEEDED TO DISTINGUISH BETWEEN CALCULATIONS
    tag = prefix.split(os.sep)[-1].split('_')[-1] + '_'
    xval = []
    yval = []
    yval2 = []
    if len(sys.argv) > 1:
        if sys.argv[1] == '-d':
            print 'calculating dipole moment'
        if int(st.states[0][0]) > int(st.states[0][1]):
            st_e = int(st.states[0][0])
            st_h = int(st.states[0][1])
        else:
            st_h = int(st.states[0][0])
            st_e = int(st.states[0][1])

        dp_name = (prefix + tag + ' dipole_moment_' + str(st_h)
                   + '_' + str(st_e) + '.txt')
        f_moment = open(dp_name, 'w')
        f_moment.write('#Dipole moment between states %i %i\n' % (st_h, st_e))
        f_moment.write('#x y z\n')
        for local_file in dn.dir_n:
            filename = os.path.join(prefix, local_file, suffix)
            dip_mom = dp.dipole(prefix=filename, no_e=st_e, no_h=st_h)
            moment = dip_mom.calc_e_h_dipole()
            print local_file.split('_')[-1], moment
            dep = float(local_file.split('_')[-1])
            f_moment.write('%e %e %e %e\n' % (dep, moment[0], moment[1],
                                              moment[2]))
            xval.append(dep)
            yval.append(moment[2])
        f_moment.close()

    if len(sys.argv) > 1:
        if sys.argv[1] == '-d3':
            print 'calculating dipole moment for nn3 wfs'
            st_e = int(st.statesNN3[0])
            st_h = int(st.statesNN3[1])

            dp_name = (prefix + tag + 'dipole_moment_' + str(st_e) + '_'
                       + str(st_h) + '.txt')
            print "dp_name: ", dp_name
            f_moment = open(dp_name, 'w')
            f_moment.write('#Dipole moment between states %i %i\n'
                           % (st_h, st_e))
            f_moment.write('#x y z\n')
            for local_file in dn.dir_n:
                filename = prefix+local_file
                dip_mom = dp.dipole(prefix=filename, no_e=st_e, no_h=st_h,
                                    Type='nn3_'+st.wftypeNN3)
                moment = dip_mom.calc_e_h_dipole()
                print local_file.split('_')[-1], moment
                dep = float(local_file.split('_')[-1])
                f_moment.write('%e %e %e %e\n' % (dep, moment[0], moment[1],
                                                  moment[2]))
                xval.append(dep)
                yval.append(moment[2])
            f_moment.close()

    if len(sys.argv) > 1:
        if sys.argv[1] == '-ex':
            print 'extracting single particle energy'
            en_pos = int(sys.argv[2])
            e_name = (prefix + tag + dn.dir_n[0].split('_')[-2] +
                      'single_particle_energy_stateNO_'+str(en_pos)+'.txt')
            f_energy = open(e_name, 'w')
            f_energy.write('#Single particle energy of state '
                           + str(en_pos)+'\n')
            f_energy.write('#var E(meV)\n')
            for local_file in dn.dir_n:
                filename = prefix+local_file+suffix+'wf_spectrum_dot_kp8.dat'
                E = na.genfromtxt(filename, unpack=True)[1][1:]
                print E[en_pos-1]
                dep = float(local_file.split('_')[-1])
                f_energy.write('%f %f\n' % (dep, E[en_pos-1]))
                xval.append(dep)
                yval.append(E[en_pos-1])
            f_energy.close()

        if len(sys.argv) > 1:
            if sys.argv[1] == '-e':
                print 'calculating transition energy'
                e_name = (prefix + tag + dn.dir_n[0].split('_')[-2] +
                          '_single_particle_energy_' + st.states[0][0] + '_to_'
                          + st.states[0][1]+'.txt')
                f_energy = open(e_name, 'w')
                f_energy.write('#Transition energy between'
                               + 'single particle states '
                               + st.states[0][0] + ' and ' +
                               st.states[0][1] + '\n')
                f_energy.write('#var E(meV)\n')
                for local_file in dn.dir_n:
                    filename = prefix+local_file+suffix
                    energ = en.energy(prefix=filename)
                    E = energ.calc_E()
                    for i in range(len(E)):
                        if (E[i][1][0] == int(st.states[0][0])
                            and E[i][1][1] == int(st.states[0][1]))\
                            or (E[i][1][1] == int(st.states[0][0])
                                and E[i][1][0] == int(st.states[0][1])):
                            print 'FOUND', E[i]
                            dep = float(local_file.split('_')[-1])
                            f_energy.write('%e %f\n' % (dep, E[i][0]))
                            xval.append(dep)
                            yval.append(E[i][0])
                f_energy.close()

        if len(sys.argv) > 1:
                if sys.argv[1] == '-e3':
                    print 'calculating transition energy for nn3'
                    e_name = prefix + tag + '_single_particle_energy.txt'
                    f_energy = open(e_name, 'w')
                    f_energy.write('#Lowest transition energy'
                                   + 'between single particle states \n')
                    f_energy.write('#var E(meV)\n')
                    for file in dn.dir_n:
                        filename = prefix+file
                        energ = en3.energy(prefix=filename,
                                           NNmode=st.wftypeNN3)
                        E = energ.calc_E()
                        dep = float(file.split('_')[-1])
                        f_energy.write('%e %f\n' % (dep, E[0][0]))
                        xval.append(dep)
                        yval.append(E[0][0])
                    f_energy.close()

        # TOTO VYKRESLI ZAVISLOST PODILU TEZKYCH,
        # LEHKYCH A SPIN-ORBIT DER NA VLNOVE FUNKCI
        if len(sys.argv) == 3:
            if sys.argv[1] == '-h':
                print 'retrieving hole compound\n'
                states = []
                for iter in sys.argv[2:]:
                    states.append(int(iter))
                in_name = 'wf_components_dot_kp8.dat'
                type = dn.dir_n[0].split('_')[-2]
                out = open(prefix + tag + 'wf_components_' + type +
                           '_st' + str(sys.argv[2]) + '.txt', 'w')
                out.write('#var cb hh lh so cb+ cb- hh+ hh- lh+ lh- so+ so-\n')
                for file in dn.dir_n:
                    infile = prefix+file+suffix+in_name
                    data = na.genfromtxt(infile, skiprows=1)  # unpack=True
                    for i in range(len(data)):
                        if int(int(data[i][0]) == states[0]):
                            print data[i][1:]
                            print file.split('_')[-1]
                            format_string = '%f '*13 + '\n'
                            out.write(format_string %
                                      (float(file.split('_')[-1]),
                                       data[i][1] + data[i][2], data[i][3] +
                                       data[i][6], data[i][4] + data[i][5],
                                       data[i][7] + data[i][8],
                                       data[i][1], data[i][2], data[i][3],
                                       data[i][6], data[i][4], data[i][5],
                                       data[i][7], data[i][8]))
                out.close()

        # usage: make_dep.py -st
        if len(sys.argv) > 1:
            print sys.argv, '\n'
            if sys.argv[1] == '-st':
                direct = sys.argv[2]
                depname = (prefix + tag + 'BiaxStrain_'
                           + str(dn.dir_n[0].split('_')[-2])
                           + '_'+direct+'Dep.txt')
                f_dep = open(depname, 'w')
                f_dep.write('#Var minPosBiax minValBiax\n')
                for directory in dn.dir_n:
                    filename = prefix+directory+suffix
                    print 'DIR', directory
                    last = float(directory.split('_')[-1])
                    type = directory.split('_')[-2]
                    outname = (prefix + 'CalcStrain_' + type + '_'
                               + str(last) + '_' + direct + '.txt')
                    f = open(outname, 'w')
                    f.write('#direction(nm) CumHydro CumDelEhhBiax\n')
                    strain = stn.elast_strain(prefix=filename)
                    data = strain.calcDerivedParam(direct)
                    minpos = na.where(data[2] == min(data[2]))
                    minval = min(data[2])
                    f_dep.write('%f %f %f\n' % (last, data[0][minpos], minval))
                    for i in range(len(data[0])):
                        f.write('%f %f %f\n' % (data[0][i],
                                                data[1][i], data[2][i]))
                        xval.append(data[0][i])
                        yval.append(data[2][i])
                    f.close()
                f_dep.close()

        if len(sys.argv) > 1:
            if sys.argv[1] == '-oNew':
                headers = {}
                headers['sppp'] = ('#Angle TME OscStr TME(sp_x)'
                                   + 'OscStr(sp_x) TME(sp_y) OscStr(sp_y)'
                                   + ' TME(sp_z) OscStr(sp_z)\n')
                headers['shls'] = ('#Angle TME OscStr TME(shh) OscStr(shh)'
                                   + 'TME(slh) OscStr(slh) TME(sso)'
                                   + 'OscStr(sso)\n')
                basis = 'sppp'  # basis Bloch waves s,px,py,pz
                extremAngPos = []
                for directory in dn.dir_n:
                    print 'DIR: ', directory
                    ax = plt.subplot(121, polar=True)
                    filename = os.path.join(prefix, directory, suffix)
                    last = float(directory.split('_')[-1])
                    print "last", last
                    start = float(sys.argv[2])
                    end = float(sys.argv[3])
                    step = int(sys.argv[4])
                    print "step: ", step  # type(step)
                    angles = na.linspace(start, end, num=step)
                    out = []
                    tempName = ('PolDepTME_' + str(st.states[0][0])
                                + '_' + str(st.states[0][1]) + '_'
                                + str(directory.split('_')[-2:]))
                    f = open(prefix + tag + tempName + '_' +
                             basis + '.txt', 'w')
                    f.write(headers[basis])
                    polarization = []

            # ###### IMPORTANT, CHOOSE ORIENTATION OF 0 DEG ##########
            for i in range(len(angles)):
                # pro orientaci 0 analyzatoru podel [100] typically pyramid QD
                # polarization.append([ na.cos(angles[i]/180.0*sp.pi) ,
                # na.sin(angles[i]/180.0*sp.pi) , 0.0 ])
                # pro orientaci 0 analyzatoru podel [010]
                # polarization.append([ na.cos((angles[i]+90)/180.0*sp.pi) ,
                # na.sin((angles[i]+90)/180.0*sp.pi) , 0.0 ])
                # pro orientaci 0 analyzatoru podel [110]
                # vypocet x podel [1-10], mereni x podel [010],
                # typically semiellipsoid QD
                # polarization.append([ na.cos((angles[i]+45)/180.0*sp.pi) ,
                # na.sin((angles[i]+45)/180.0*sp.pi) , 0.0 ])
                # pro orientaci 0 analyzatoru podel [1-10]
                polarization.append([na.cos((angles[i] - 45) / 180.0 * sp.pi),
                                     na.sin((angles[i] - 45) / 180.0 * sp.pi),
                                     0.0])
                # pro polarizaci podel [001]
                # polarization.append([ 0.0 , na.cos((angles[i]+90)/180.0
                # *sp.pi),
                # na.sin((angles[i]+90)/180.0*sp.pi) ])
                # angle_z = 10
                # polarization.append([ na.cos((angles[i]+45)/180.0*sp.pi),
                # na.sin((angles[i]+45)/180.0*sp.pi)*na.cos((angle_z)/180.0
                # *sp.pi) , na.sin((angle_z)/180.0*sp.pi) ])
            import transition_probab_v1 as trans
            my_trans = trans.trans_probab(prefix=filename)
            pr = cProfile.Profile()
            pr.enable()
            data = my_trans.makePolDep(polarization, basisType=basis)
            pr.disable()
            s = StringIO.StringIO()
            sortby = 'cumulative'
            ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
            ps.print_stats()
            ps.dump_stats("stat_file.txt")
            print s.getvalue()
            for i in range(len(angles)):
                out.append([angles[i],
                            data[0][i], data[1][i], data[2][i], data[3][i],
                            data[4][i], data[5][i], data[6][i], data[7][i]])
            for i in range(len(angles)):
                f.write('%f %f %f %f %f %f %f %f %f\n' % (out[i][0],
                                                          out[i][1], out[i][2],
                                                          out[i][3], out[i][4],
                                                          out[i][5], out[i][6],
                                                          out[i][7],
                                                          out[i][8]))
            posMax = data[1].index(max(data[1]))
            posMin = data[1].index(min(data[1]))
            valMax = max(data[1])
            valMin = min(data[1])
            polDegree = (valMax-valMin)/(valMax+valMin)
            print ('Angular position of maximum, minimum: ',
                   angles[int(posMax)], angles[int(posMin)],
                   'value at maximum, minimum: ',
                   valMax, valMin, 'polDegree: ', polDegree, '\n\n')
            if angles[int(posMax)] > 0:
                ratio = valMax / valMin
            else:
                ratio = valMin / valMax
            extremAngPos.append([float(last), angles[int(posMax)],
                                 angles[int(posMin)], ratio,
                                 valMax, valMin, polDegree])
            f.close()
            ax.plot(angles * na.pi / 180.0, data[1] - min(data[1]),
                    'o', label=last)
            ax.grid(True)
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc=2, borderaxespad=1.)
        plt.savefig(prefix + tag + 'angOSC_' + st.states[0][0]
                    + '_' + st.states[0][1] + '_' + basis + '.png')
        plt.show()
        fAng = open(prefix + tag + 'angPos_' + st.states[0][0] + '_'
                    + st.states[0][1] + '_' + basis + '.txt', 'w')
        fAng.write('#Var max(deg) min(deg) Val[110]/Val[1-10]'
                   + 'ValMax ValMin PolDegree\n')
        for i in range(len(extremAngPos)):
            fAng.write('%e %f %f %e %e %e %e\n' %
                       (extremAngPos[i][0], extremAngPos[i][1],
                        extremAngPos[i][2], extremAngPos[i][3],
                        extremAngPos[i][4], extremAngPos[i][5],
                        extremAngPos[i][6]))
            xval.append(extremAngPos[i][0])
            yval.append(extremAngPos[i][6])
            yval2.append(extremAngPos[i][3])
        fAng.close()

        if len(sys.argv) > 1:
            if sys.argv[1] == '-oNN':
                NNoscStNames = [
                    'transitions_dot_pol1.dat',
                    'transitions_dot_pol2.dat']
                states = [4, 5]
                out = open(prefix + tag
                           + 'osc_strength_NN.txt', 'w')
                out.write('#Val')
                for data in NNoscStNames:
                    pol = data.split('.')[0].split('_')[-1]
                    out.write(' %s' % (str(pol)))
                out.write('\n')
                for directory in dn.dir_n:
                    filename = prefix+directory+suffix
                    print directory
                    last = float(directory.split('_')[-1])
                    out.write('%f' % (last))
                    for i in range(len(NNoscStNames)):
                        file = filename+NNoscStNames[i]
                        f = open(file, 'r')
                        buf = na.loadtxt(file, skiprows=1, unpack=True)
                for j in range(len(buf[0])):
                    if buf[1][j] == states[0] and buf[2][j] == states[1]:
                        print buf[3][j]
                        out.write(' %f' % (float(buf[3][j])))
                out.write('\n')
                out.close()

        # convert to vtk file for 3D data imaging by mayavi
        if len(sys.argv) > 1:
            if sys.argv[1] == '-vtk':
                if len(sys.argv) == 3:
                    st = int(sys.argv[2])
                    stName = 'wf_probability_dot_kp8_0000_000' + str(st)
                    if st >= 10:
                        stName += '.dat'
                    for dir in dn.dir_n:
                        may.conv(prefix + dir + suffix,
                                 stName, prefix, dir+'_st'+str(st))
                elif len(sys.argv) == 2:
                    Name = 'alloy_composition'
                    for dir in dn.dir_n:
                        may.conv(prefix + dir + suffix,
                                 Name, prefix, dir+'_'+str(Name))

        if len(sys.argv) > 2:
            if sys.argv[1] == '-sl':
                print sys.argv
                plt.clf()
                datmax = -1e3
                datmin = 1e3
                datas = []
                datasMat = []
                var = []
                for j in range(len(dn.dir_n)):
                    file = dn.dir_n[j]
                    print file
                    var.append(file.split('_')[-1])
                    filename = prefix+file+suffix+dn.sliceName
                    matname = prefix+file+suffix+dn.matName
                    cut = sl.makeCut(filename)
                    datmax = -1e3
                    datmin = 1e3
                    temp = []
                    tempMat = []
                    for i in range(len(dn.directions)):
                        direct = dn.directions[i]
                        slice = cut.sliceAnyDirec(name=filename,
                                                  vec1=direct[0],
                                                  vec2=direct[1], isProbab=1)
                        data = slice[0]
                        ext = slice[1]
                        datCoords = slice[2]
                        print 'EXT WF ', ext
                        temp.append([data, ext])
                        sliceMat = cut.sliceAnyDirec(name=matname,
                                                     vec1=direct[0],
                                                     vec2=direct[1],
                                                     isProbab=0,
                                                     ord=0,
                                                     loadMatCoord=datCoords)
                        dataMat = sliceMat[0]
                        extMat = sliceMat[1]
                        print 'EXT MAT ', extMat
                        tempMat.append([dataMat, extMat])
                    datas.append(temp)
                    datasMat.append(tempMat)
                    print 'DATAS'
                    print len(datas), len(datas[0])
                    print 'DATASMAT'
                    print len(datasMat), len(datasMat[0])

                    datmax = -1e3
                    datmin = 1e3
                    LatN = 1e3
                    LatP = -1e3
                    VerN = 1e3
                    VerP = -1e3
                    for i in range(len(datas)):
                        for j in range(len(datas[i])):
                            if abs(datas[i][j][0]).min() < datmin:
                                datmin = abs(datas[i][j][0]).min()
                            if abs(datas[i][j][0]).max() > datmax:
                                datmax = abs(datas[i][j][0]).max()
                            if datas[i][j][1][0] < LatN:
                                LatN = datas[i][j][1][0]
                            if datas[i][j][1][1] > LatP:
                                LatP = datas[i][j][1][1]
                            if datas[i][j][1][2] < VerN:
                                VerN = datas[i][j][1][2]
                            if datas[i][j][1][3] > VerP:
                                VerP = datas[i][j][1][3]
                    ext = na.array([LatN, LatP, VerN, VerP])
                    if sys.argv[2] == 'fig':
                        print 'FIGURE GENERATION'
                        fig, axs = plt.subplots(len(datas), len(datas[0]),
                                                sharex=True)
                        for i in range(len(datas)):
                            for j in range(len(datas[i])):
                                print i, j
                                dat = datas[i][j][0]
                                im = axs[i, j].imshow(dat, cmap='Spectral_r',
                                                      origin='lower',
                                                      vmin=datmin,
                                                      vmax=datmax,
                                                      extent=ext,
                                                      aspect='auto')
                                im.set_interpolation('nearest')
                                datM = datasMat[i][j][0]
                                levMat = na.array([32.0, 34.0])
                                print "levMat: ", levMat
                                plt.text(0.1, 0.9, str(var[i])+' nm',
                                         ha='center', va='center',
                                         transform=axs[i, j].transAxes)
                                if i == len(datas)-1:
                                    if dn.directions[j][0] == [0, 1, 0]:
                                        dirout = [1, 1, 0]
                                    elif dn.directions[j][0] == [1, 0, 0]:
                                        dirout = [1, -1, 0]
                                    else:
                                        dirout = dn.directions[j][0]
                                        axs[i, j].set_xlabel(str(dirout)
                                                             + ' (nm)')
                        fig.subplots_adjust(hspace=0.1)
                        fig.text(0.06, 0.5, str(dn.directions[0][1])+' (nm)',
                                 ha='center', va='center', rotation='vertical')
                        fig.subplots_adjust(right=0.8)
                        cbar_ax = fig.add_axes([0.85, 0.15, 0.02, 0.7])
                        fig.colorbar(im, cax=cbar_ax)
                        outname = (prefix + dn.sliceName
                                   + '_' + str(dn.directions[0][1]))
                        plt.savefig(outname+'.png')
                        plt.savefig(outname+'.eps')
                        plt.show()

                    elif sys.argv[2] == 'vid':
                        print 'VIDEO GENERATION'
                        mpeg_location = 'c:\\ffmpeg\\bin\\ffmpeg.exe'
                        plt.rcParams['animation.ffmpeg_path'] = mpeg_location
                        fig, axs = plt.subplots(1, len(datas[0]), sharex=True)
                        ims = []
                        datVid = []
                        for i in range(len(datas)):
                            imsIn = []
                            tempVid = []
                            for j in range(len(datas[i])):
                                print i, j
                                dat = datas[i][j][0]
                                tempVid.append(dat)
                                im = axs[j].imshow(dat, cmap='Spectral_r',
                                                   origin='lower', vmin=datmin,
                                                   vmax=datmax, extent=ext,
                                                   aspect='auto')
                                im.set_interpolation('nearest')
                                datM = datasMat[i][j][0]
                                levMat = na.array([32.0, 34.0])
                                print levMat
                                imsIn.append(im)
                            ims.append(imsIn)
                            datVid.append(datas[i][0][0])
                        print 'VIDEO GENERATED'
                        vidFileName = (prefix+dn.sliceName+'_'
                                       + str(dn.directions[0][1])+'_anim.mp4')
                        print vidFileName
                        datVida = na.array(datVid)
                        print datVida[0], datVida[0][0]
                        gif.writeGif(vidFileName, datVida, duration=10,
                                     repeat=True, dither=False, nq=10)
                        plt.show()

        #   PLOT OF THE CALCULATED QUANTITY
        plt.clf()
        plt.plot(xval, yval, marker='o', linestyle='-',
                 linewidth=2, label='yval')
        if len(xval) == len(yval2):
            plt.plot(xval, yval2, marker='o',
                     linestyle='-', linewidth=2, label='yval2')
        plt.legend()
        plt.show()
        plt.clf()

if __name__ == '__main__':
    main()
